import json

from clinicaltrials.models import GetFieldValuesInput
from clinicaltrials.utils import CT_API_BASE_URL, _handle_api_error, make_api_client


def register_get_field_values(mcp) -> None:
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
