from typing import List
from pydantic import BaseModel, Field, ConfigDict, field_validator

from clinicaltrials.models.fields import (
    STUDY_FIELDS_SKILL_RESOURCE,
    validate_study_fields,
)


class GetFieldValuesInput(BaseModel):
    """Input parameters for the GET /stats/fieldValues endpoint."""
    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid",
    )

    fields: List[str] = Field(
        ...,
        min_length=1,
        description=(
            "One or more study field names to retrieve value distributions for. "
            "Works best with enumerable fields like Phase, OverallStatus, StudyType, "
            "Sex, StdAge, LeadSponsorClass, InterventionType, LocationCountry. "
            "Each field returns its top values ranked by study count. "
            f"For the full list of valid field names, read the resource {STUDY_FIELDS_SKILL_RESOURCE}."
        ),
    )

    @field_validator("fields")
    @classmethod
    def _validate_fields(cls, v):
        return validate_study_fields(v)
