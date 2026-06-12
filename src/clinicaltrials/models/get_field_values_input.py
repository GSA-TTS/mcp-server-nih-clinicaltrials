from typing import List
from pydantic import BaseModel, Field, ConfigDict

from clinicaltrials.models.fields import StudyField


class GetFieldValuesInput(BaseModel):
    """Input parameters for the GET /stats/fieldValues endpoint."""
    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid",
    )

    fields: List[StudyField] = Field(
        ...,
        min_length=1,
        description=(
            "One or more study fields to retrieve value distributions for. "
            "Works best with enumerable fields like Phase, OverallStatus, StudyType, "
            "Sex, StdAge, LeadSponsorClass, InterventionType, LocationCountry. "
            "Each field returns its top values ranked by study count."
        ),
    )
