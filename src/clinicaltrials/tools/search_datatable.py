from typing import Any

from clinicaltrials.models import SearchDatatableInput
from clinicaltrials.utils import CT_API_BASE_URL, _handle_api_error, make_api_client
from prefab_ui.app import PrefabApp
from prefab_ui.components import Column, DataTable, DataTableColumn, Heading


def register_search_datatable(mcp) -> None:
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
