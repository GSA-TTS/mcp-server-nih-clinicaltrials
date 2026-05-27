import json
from typing import Any

from clinicaltrials.models import AnalyzeStudyLocationsInput
from clinicaltrials.utils import CT_API_BASE_URL, _handle_api_error, make_api_client


def register_analyze_locations(mcp) -> None:
    @mcp.tool(
        name="analyze_study_locations",
        annotations={
            "title": "Analyze Study Locations by Country",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": True,
        },
    )
    async def analyze_study_locations(
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
