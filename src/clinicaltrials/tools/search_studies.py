import json
from typing import Any

from clinicaltrials.models import ResponseFormat, SearchStudiesInput
from clinicaltrials.utils import CT_API_BASE_URL, _handle_api_error, make_api_client


def register_search_studies(mcp) -> None:
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
                - query_locn (Optional[str]): Location search supporting text or AREA syntax.
                  Simple: 'Boston', 'Mayo Clinic'. AREA: 'AREA[LocationState]MA', 'AREA[LocationCountry]US'.
                - query_patient (Optional[str]): Plain-language patient-friendly search.

                Filters:
                - filter_overall_status (Optional[List[OverallStatus]]): Limit by recruitment status.
                - filter_geo (Optional[str]): Geographic radius, e.g. 'distance(39.0,-77.0,50mi)'.
                - filter_ids (Optional[List[str]]): Specific NCT IDs to retrieve.
                - filter_advanced (Optional[str]): Advanced Essie expression syntax filter.
                  Examples: 'AREA[StartDate]2022' or 'AREA[MinimumAge]RANGE[MIN, 16 years] AND AREA[MaximumAge]RANGE[16 years, MAX]'.
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

        if params.filter_overall_status:
            query_params["filter.overallStatus"] = ",".join(
                s.value for s in params.filter_overall_status
            )
        if params.filter_geo:
            query_params["filter.geo"] = params.filter_geo
        if params.filter_ids:
            query_params["filter.ids"] = ",".join(params.filter_ids)
        if params.filter_advanced:
            query_params["filter.advanced"] = params.filter_advanced
        if params.post_filter_overall_status:
            query_params["postFilter.overallStatus"] = ",".join(
                s.value for s in params.post_filter_overall_status
            )
        if params.post_filter_geo:
            query_params["postFilter.geo"] = params.post_filter_geo
        if params.agg_filters:
            query_params["aggFilters"] = params.agg_filters
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
