import json
from typing import Any

from clinicaltrials.models import GetStudyInput, ResponseFormat
from clinicaltrials.utils import CT_API_BASE_URL, _handle_api_error, make_api_client


def register_get_study(mcp) -> None:
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
