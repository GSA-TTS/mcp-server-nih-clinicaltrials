import json
from typing import Any

from clinicaltrials.models import (
    AnalyzeStudyLocationsInput,
    GetFieldValuesInput,
    GetStudyInput,
    ResponseFormat,
    SearchDatatableInput,
    SearchStudiesInput,
)
from clinicaltrials.utils import _handle_api_error, make_api_client
from prefab_ui.app import PrefabApp
from prefab_ui.components import Column, DataTable, DataTableColumn, Heading


CT_API_BASE_URL = "https://clinicaltrials.gov/api/v2"


def register_tools(mcp) -> None:
    """Register all ClinicalTrials.gov tools with the MCP server."""

    @mcp.tool(
        name="clinicaltrials_get_study",
        annotations={
            "title": "Get Clinical Study by NCT ID",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": True,
        },
    )
    async def clinicaltrials_get_study(params: GetStudyInput) -> str:
        """Retrieve a single clinical study record from ClinicalTrials.gov by its NCT identifier.

        Fetches the full study record (or a filtered subset of fields) for a given NCT ID
        from the ClinicalTrials.gov v2 API.

        Args:
            params (GetStudyInput): Validated input parameters containing:
                - nct_id (str): NCT study identifier, e.g. 'NCT00000102'. Must match pattern NCT\\d+.
                - format (ResponseFormat): 'json' (default) or 'csv'.
                - markup_format (MarkupFormat): 'markdown' (default) or 'legacy' for text fields.
                - fields (Optional[str]): Comma-separated field names to include, e.g.
                  'NCTId,BriefTitle,OverallStatus,Phase'. Omit to return all fields.

        Returns:
            str: The study data as a JSON string (when format='json') or CSV text
            (when format='csv'), or an error message string prefixed with 'Error:'.

            JSON success response schema (top-level keys):
            {
                "protocolSection": {
                    "identificationModule": {"nctId": str, "briefTitle": str, ...},
                    "statusModule": {"overallStatus": str, ...},
                    "descriptionModule": {"briefSummary": str, ...},
                    "conditionsModule": {"conditions": [str], ...},
                    "designModule": {"studyType": str, "phases": [str], ...},
                    "eligibilityModule": {"eligibilityCriteria": str, "sex": str, ...},
                    "contactsLocationsModule": {"locations": [...], ...},
                    ...
                },
                "derivedSection": {...},
                "hasResults": bool
            }

            Error responses:
            - "Error: Study not found. Verify the NCT ID is correct."
            - "Error: Rate limit exceeded. Please wait before retrying."
            - "Error: Request timed out. Please try again."

        Fields not available via this API (inform the user if asked):
            - Version number: studies do not carry a version identifier
            - Protocol amendment history: individual amendment versions are not exposed
            - IRB approval documents: not accessible via the API
            - Raw protocol/SAP/ICF files: LargeDoc fields return metadata only, not file contents
            - Regulatory submission IDs (IND, IDE numbers): not surfaced as structured fields
            - Full investigator contact details: name and role are available but phone/email
              are only sometimes present and are not guaranteed

        Examples:
            - Use when: "Get full details for NCT00000102"
              → params with nct_id='NCT00000102'
            - Use when: "What is the status and phase of study NCT04280705?"
              → params with nct_id='NCT04280705', fields='NCTId,OverallStatus,Phase'
            - Don't use when: Searching studies by condition or sponsor (use a search tool instead).
        """
        query_params: dict[str, Any] = {
            "format": params.format.value,
            "markupFormat": params.markup_format.value,
        }
        if params.fields:
            query_params["fields"] = ",".join(f.value for f in params.fields)

        try:
            async with make_api_client() as client:
                response = await client.get(
                    f"{CT_API_BASE_URL}/studies/{params.nct_id}",
                    params=query_params,
                    timeout=30.0,
                )
                response.raise_for_status()
        except Exception as e:
            return _handle_api_error(e)

        if params.format == ResponseFormat.JSON:
            return json.dumps(response.json(), indent=2)
        return response.text

    @mcp.tool(
        name="clinicaltrials_search_studies",
        annotations={
            "title": "Search Clinical Studies",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": True,
        },
    )
    async def clinicaltrials_search_studies(params: SearchStudiesInput) -> str:
        """Search for clinical studies on ClinicalTrials.gov using conditions, interventions, sponsors, and more.

        Queries the ClinicalTrials.gov v2 API search endpoint and returns a paginated
        list of matching studies. At least one query parameter or filter_ids must be provided.

        Args:
            params (SearchStudiesInput): Validated search parameters containing:
                Query fields (at least one required):
                - query_cond (Optional[str]): Condition or disease (e.g., 'diabetes').
                - query_term (Optional[str]): General keyword search (e.g., 'mRNA vaccine').
                - query_intr (Optional[str]): Intervention name (e.g., 'insulin').
                - query_titles (Optional[str]): Search within study titles only.
                - query_id (Optional[str]): Study ID or NCT number. Note: regulatory
                  submission IDs such as IND or IDE numbers are not searchable fields
                  in the API and will not match via this parameter.
                - query_spons (Optional[str]): Sponsor or collaborator name (e.g., 'NIH').
                - query_locn (Optional[str]): Location terms (e.g., 'Boston').
                - query_patient (Optional[str]): Plain-language patient-friendly search.

                Filters:
                - filter_overall_status (Optional[List[OverallStatus]]): Limit by recruitment status.
                - filter_geo (Optional[str]): Geographic radius, e.g. 'distance(39.0,-77.0,50mi)'.
                - filter_ids (Optional[List[str]]): Specific NCT IDs to retrieve.
                - post_filter_overall_status (Optional[List[OverallStatus]]): Status filter applied after aggregation.
                - post_filter_geo (Optional[str]): Geo filter applied after aggregation.
                - agg_filters (Optional[str]): Aggregation filters string, e.g. 'phase:2 3,studyType:int'.

                Sorting & pagination:
                - sort (Optional[str]): Sort field and direction, e.g. 'LastUpdatePostDate:desc'.
                - page_size (int): Results per page, 1–1000 (default 20).
                - page_token (Optional[str]): Cursor from a previous response's 'nextPageToken'.
                - count_total (bool): Include total match count in response (default False).

                Output:
                - format (ResponseFormat): 'json' (default) or 'csv'.
                - markup_format (MarkupFormat): 'markdown' (default) or 'legacy'.
                - fields (Optional[str]): Comma-separated fields to return.

        Returns:
            str: JSON string or CSV text, or an error message prefixed with 'Error:'.

            JSON success response schema:
            {
                "totalCount": int,          # Only present when count_total=True
                "studies": [
                    {
                        "protocolSection": {
                            "identificationModule": {"nctId": str, "briefTitle": str, ...},
                            "statusModule": {"overallStatus": str, ...},
                            ...
                        },
                        ...
                    }
                ],
                "nextPageToken": str        # Present when more pages exist; pass to page_token for next page
            }

            Error responses:
            - "Error: Bad request — check your parameters."
            - "Error: Rate limit exceeded. Please wait before retrying."
            - "Error: Request timed out. Please try again."

        Examples:
            - Use when: "Find recruiting Phase 3 diabetes trials"
              → query_cond='diabetes', filter_overall_status=[RECRUITING], agg_filters='phase:3'
            - Use when: "Search for NIH-sponsored cancer studies updated recently"
              → query_cond='cancer', query_spons='NIH', sort='LastUpdatePostDate:desc'
            - Use when: "Find trials near Boston for asthma"
              → query_cond='asthma', filter_geo='distance(42.36,-71.06,25mi)'
            - Use when: "Get details for these specific studies: NCT04280705, NCT00000102"
              → filter_ids=['NCT04280705', 'NCT00000102']
            - Don't use when: You have a single NCT ID and want full details (use clinicaltrials_get_study instead).
        """
        query_params: dict[str, Any] = {
            "format": params.format.value,
            "markupFormat": params.markup_format.value,
            "pageSize": params.page_size,
            "countTotal": str(params.count_total).lower(),
        }

        # Query fields — API uses dot notation (e.g., query.cond)
        query_map = {
            "query.cond": params.query_cond,
            "query.term": params.query_term,
            "query.intr": params.query_intr,
            "query.titles": params.query_titles,
            "query.id": params.query_id,
            "query.spons": params.query_spons,
            "query.locn": params.query_locn,
            "query.patient": params.query_patient,
        }
        for key, value in query_map.items():
            if value is not None:
                query_params[key] = value

        # Filters
        if params.filter_overall_status:
            query_params["filter.overallStatus"] = ",".join(
                s.value for s in params.filter_overall_status
            )
        if params.filter_geo:
            query_params["filter.geo"] = params.filter_geo
        if params.filter_ids:
            query_params["filter.ids"] = ",".join(params.filter_ids)
        if params.post_filter_overall_status:
            query_params["postFilter.overallStatus"] = ",".join(
                s.value for s in params.post_filter_overall_status
            )
        if params.post_filter_geo:
            query_params["postFilter.geo"] = params.post_filter_geo
        if params.agg_filters:
            query_params["aggFilters"] = params.agg_filters

        # Optional output params
        if params.sort:
            query_params["sort"] = params.sort
        if params.page_token:
            query_params["pageToken"] = params.page_token
        if params.fields:
            query_params["fields"] = ",".join(f.value for f in params.fields)

        try:
            async with make_api_client() as client:
                response = await client.get(
                    f"{CT_API_BASE_URL}/studies",
                    params=query_params,
                    timeout=30.0,
                )
                response.raise_for_status()
        except Exception as e:
            return _handle_api_error(e)

        if params.format == ResponseFormat.JSON:
            return json.dumps(response.json(), indent=2)
        return response.text

    @mcp.tool(
        name="clinicaltrials_get_field_values",
        annotations={
            "title": "Get Field Value Distributions",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": True,
        },
    )
    async def clinicaltrials_get_field_values(params: GetFieldValuesInput) -> str:
        """Get the distribution of values across all studies for one or more fields.

        Queries the ClinicalTrials.gov /stats/fieldValues endpoint to return how many
        studies have each distinct value for the requested fields. Most useful for
        enumerable fields; free-text fields return only the top values by frequency.

        Args:
            params (GetFieldValuesInput): Input containing:
                - fields (List[StudyField]): One or more fields to get distributions for.
                  Best used with enumerable fields such as:
                    Phase, OverallStatus, StudyType, Sex, StdAge,
                    LeadSponsorClass, InterventionType, LocationCountry,
                    DesignAllocation, DesignPrimaryPurpose, DesignMasking,
                    IsFDARegulatedDrug, HasResults, IPDSharing.

        Returns:
            str: JSON array where each element corresponds to one requested field:
            [
                {
                    "type": str,                # "ENUM" or "STRING"
                    "piece": str,               # Field name (matches StudyField value)
                    "field": str,               # Full JSON path in the study record
                    "missingStudiesCount": int, # Studies where this field is absent
                    "uniqueValuesCount": int,   # Total distinct values
                    "topValues": [
                        {"value": str, "studiesCount": int},
                        ...
                    ]
                },
                ...
            ]
            Or an error message string prefixed with "Error:".

        Examples:
            - Use when: "How many studies are in each phase?"
              → fields=[StudyField.Phase]
            - Use when: "What's the breakdown of recruiting status and study type?"
              → fields=[StudyField.OverallStatus, StudyField.StudyType]
            - Use when: "Which countries have the most trial locations?"
              → fields=[StudyField.LocationCountry]
            - Don't use when: You want full study records (use clinicaltrials_search_studies).
        """
        fields_param = ",".join(f.value for f in params.fields)

        try:
            async with make_api_client() as client:
                response = await client.get(
                    f"{CT_API_BASE_URL}/stats/fieldValues",
                    params={"fields": fields_param},
                    timeout=30.0,
                )
                response.raise_for_status()
        except Exception as e:
            return _handle_api_error(e)

        return json.dumps(response.json(), indent=2)

    @mcp.tool(
        name="clinicaltrials_analyze_study_locations",
        annotations={
            "title": "Analyze Study Locations by Country",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": True,
        },
    )
    async def clinicaltrials_analyze_study_locations(
        params: AnalyzeStudyLocationsInput,
    ) -> str:
        """Analyze the country distribution of locations across a cohort of clinical studies.

        Executes a search using the provided query/filter parameters, pages through all
        matching results, and classifies each study into one of four categories relative
        to a target country:
          - only_in_target: all locations are in the target country
          - mixed: locations in both the target country and at least one other country
          - not_in_target: no locations in the target country
          - no_location_data: no location country data present for the study

        Also returns a frequency table of every country seen, sorted by count descending.
        Only NCTId and LocationCountry fields are fetched per page to minimize payload size.
        For large cohorts (e.g., 196,000 studies) this may take several minutes.

        Args:
            params (AnalyzeStudyLocationsInput): Search/filter parameters plus:
                Query fields (at least one required):
                - query_cond, query_term, query_intr, query_titles, query_id,
                  query_spons, query_locn, query_patient

                Filters:
                - filter_overall_status, filter_geo, filter_ids,
                  post_filter_overall_status, post_filter_geo, agg_filters

                Analysis:
                - target_country (str): Reference country (default: 'United States').
                  Comparison is case-insensitive.

        Returns:
            str: JSON string with the following structure, or an error string prefixed 'Error:'.
            {
                "summary": {
                    "total_found": int,
                    "target_country": str,
                    "only_in_target": int,
                    "mixed": int,
                    "not_in_target": int,
                    "no_location_data": int
                },
                "country_frequency": {        # all countries seen, sorted by count desc
                    "United States": int,
                    "Germany": int,
                    ...
                }
            }

        Examples:
            - Use when: "How many recruiting diabetes trials are US-only?"
              → query_cond='diabetes', filter_overall_status=[RECRUITING]
            - Use when: "Of all NIH-sponsored studies, which are exclusively in the US?"
              → query_spons='NIH', target_country='United States'
            - Use when: "Analyze locations for these specific studies"
              → filter_ids=['NCT04280705', 'NCT00000102']
            - Don't use when: You want full study details (use clinicaltrials_get_study).
            - Don't use when: You only need a paginated list (use clinicaltrials_search_studies).
        """
        target_lower = params.target_country.strip().lower()
        target_display = params.target_country.strip()

        only_in_target = 0
        mixed = 0
        not_in_target = 0
        no_location_data = 0
        total_found = 0
        country_freq: dict[str, int] = {}

        base_params: dict[str, Any] = {
            "format": "json",
            "pageSize": 1000,
            "fields": "NCTId,LocationCountry",
            "countTotal": "false",
        }

        query_map = {
            "query.cond": params.query_cond,
            "query.term": params.query_term,
            "query.intr": params.query_intr,
            "query.titles": params.query_titles,
            "query.id": params.query_id,
            "query.spons": params.query_spons,
            "query.locn": params.query_locn,
            "query.patient": params.query_patient,
        }
        for key, value in query_map.items():
            if value is not None:
                base_params[key] = value

        if params.filter_overall_status:
            base_params["filter.overallStatus"] = ",".join(
                s.value for s in params.filter_overall_status
            )
        if params.filter_geo:
            base_params["filter.geo"] = params.filter_geo
        if params.filter_ids:
            base_params["filter.ids"] = ",".join(params.filter_ids)
        if params.post_filter_overall_status:
            base_params["postFilter.overallStatus"] = ",".join(
                s.value for s in params.post_filter_overall_status
            )
        if params.post_filter_geo:
            base_params["postFilter.geo"] = params.post_filter_geo
        if params.agg_filters:
            base_params["aggFilters"] = params.agg_filters

        page_token = None
        while True:
            query_params = dict(base_params)
            if page_token:
                query_params["pageToken"] = page_token

            try:
                async with make_api_client() as client:
                    response = await client.get(
                        f"{CT_API_BASE_URL}/studies",
                        params=query_params,
                        timeout=60.0,
                    )
                    response.raise_for_status()
            except Exception as e:
                return _handle_api_error(e)

            data = response.json()
            for study in data.get("studies", []):
                total_found += 1
                locations = (
                    study.get("protocolSection", {})
                    .get("contactsLocationsModule", {})
                    .get("locations", [])
                )
                countries = {
                    loc["country"].strip()
                    for loc in locations
                    if loc.get("country")
                }
                for c in countries:
                    country_freq[c] = country_freq.get(c, 0) + 1

                if not countries:
                    no_location_data += 1
                elif all(c.lower() == target_lower for c in countries):
                    only_in_target += 1
                elif any(c.lower() == target_lower for c in countries):
                    mixed += 1
                else:
                    not_in_target += 1

            page_token = data.get("nextPageToken")
            if not page_token:
                break

        sorted_countries = dict(
            sorted(country_freq.items(), key=lambda x: x[1], reverse=True)
        )

        return json.dumps(
            {
                "summary": {
                    "total_found": total_found,
                    "target_country": target_display,
                    "only_in_target": only_in_target,
                    "mixed": mixed,
                    "not_in_target": not_in_target,
                    "no_location_data": no_location_data,
                },
                "country_frequency": sorted_countries,
            },
            indent=2,
        )

    @mcp.tool(app=True)
    async def clinicaltrials_search_datatable(params: SearchDatatableInput) -> PrefabApp:
        """
        Search clinical studies and display all matching results as an interactive table.

        Use this instead of clinicaltrials_search_studies when you want results rendered
        as a sortable, searchable, paginated table rather than raw JSON. Fetches all
        matching studies across all pages and loads them into a single DataTable.
        Each row shows NCT ID, title, status, phase, conditions, interventions,
        sponsor, start date, and enrollment count.

        Args:
            params (SearchDatatableInput): Search/filter parameters plus:
                Query fields (at least one required):
                - query_cond, query_term, query_intr, query_titles, query_id,
                  query_spons, query_locn, query_patient
                  Note: query_id accepts NCT IDs and secondary identifiers but not
                  regulatory submission IDs (IND, IDE numbers), which are not
                  searchable fields in the API.

                Filters:
                - filter_overall_status, filter_geo, filter_ids,
                  post_filter_overall_status, post_filter_geo, agg_filters

                Sorting:
                - sort (str): e.g. 'LastUpdatePostDate:desc'.

        Returns:
            PrefabApp: Interactive DataTable with all matching study results.
        """
        base_params: dict[str, Any] = {
            "format": "json",
            "pageSize": 1000,
            "fields": (
                "NCTId,BriefTitle,OverallStatus,Phase,Condition,"
                "InterventionName,LeadSponsorName,StartDate,EnrollmentCount"
            ),
            "countTotal": "false",
        }

        query_map = {
            "query.cond": params.query_cond,
            "query.term": params.query_term,
            "query.intr": params.query_intr,
            "query.titles": params.query_titles,
            "query.id": params.query_id,
            "query.spons": params.query_spons,
            "query.locn": params.query_locn,
            "query.patient": params.query_patient,
        }
        for key, value in query_map.items():
            if value is not None:
                base_params[key] = value

        if params.filter_overall_status:
            base_params["filter.overallStatus"] = ",".join(
                s.value for s in params.filter_overall_status
            )
        if params.filter_geo:
            base_params["filter.geo"] = params.filter_geo
        if params.filter_ids:
            base_params["filter.ids"] = ",".join(params.filter_ids)
        if params.post_filter_overall_status:
            base_params["postFilter.overallStatus"] = ",".join(
                s.value for s in params.post_filter_overall_status
            )
        if params.post_filter_geo:
            base_params["postFilter.geo"] = params.post_filter_geo
        if params.agg_filters:
            base_params["aggFilters"] = params.agg_filters
        if params.sort:
            base_params["sort"] = params.sort

        rows = []
        page_token = None
        while True:
            query_params = dict(base_params)
            if page_token:
                query_params["pageToken"] = page_token

            try:
                async with make_api_client() as client:
                    response = await client.get(
                        f"{CT_API_BASE_URL}/studies",
                        params=query_params,
                        timeout=60.0,
                    )
                    response.raise_for_status()
            except Exception as e:
                raise RuntimeError(_handle_api_error(e))

            data = response.json()
            for study in data.get("studies", []):
                p = study.get("protocolSection", {})
                id_mod = p.get("identificationModule", {})
                status_mod = p.get("statusModule", {})
                conditions_mod = p.get("conditionsModule", {})
                design_mod = p.get("designModule", {})
                arms_mod = p.get("armsInterventionsModule", {})
                sponsor_mod = p.get("sponsorCollaboratorsModule", {})

                raw_phases = design_mod.get("phases", [])
                phase_str = ", ".join(
                    ph.replace("PHASE", "Phase ").replace("NA", "N/A")
                    for ph in raw_phases
                )

                interventions = [
                    i["name"] for i in arms_mod.get("interventions", []) if i.get("name")
                ]

                rows.append({
                    "nct_id": id_mod.get("nctId", ""),
                    "title": id_mod.get("briefTitle", ""),
                    "status": status_mod.get("overallStatus", ""),
                    "phase": phase_str,
                    "conditions": ", ".join(conditions_mod.get("conditions", [])),
                    "interventions": ", ".join(interventions),
                    "sponsor": (sponsor_mod.get("leadSponsor") or {}).get("name", ""),
                    "start_date": (status_mod.get("startDateStruct") or {}).get("date", ""),
                    "enrollment": (design_mod.get("enrollmentInfo") or {}).get("count"),
                })

            page_token = data.get("nextPageToken")
            if not page_token:
                break

        with PrefabApp() as app:
            with Column(gap=4, css_class="p-6"):
                Heading(f"ClinicalTrials.gov Results ({len(rows):,} studies)")
                DataTable(
                    columns=[
                        DataTableColumn(key="nct_id",        header="NCT ID",       sortable=True),
                        DataTableColumn(key="title",         header="Title",         sortable=True),
                        DataTableColumn(key="status",        header="Status",        sortable=True),
                        DataTableColumn(key="phase",         header="Phase",         sortable=True),
                        DataTableColumn(key="conditions",    header="Conditions",    sortable=False),
                        DataTableColumn(key="interventions", header="Interventions", sortable=False),
                        DataTableColumn(key="sponsor",       header="Sponsor",       sortable=True),
                        DataTableColumn(key="start_date",    header="Start Date",    sortable=True),
                        DataTableColumn(key="enrollment",    header="Enrollment",    sortable=True),
                    ],
                    rows=rows,
                    search=True,
                    paginated=True,
                    page_size=20,
                )

        return app
