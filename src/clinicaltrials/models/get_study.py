from typing import Optional, List
from pydantic import BaseModel, Field, field_validator, ConfigDict

from clinicaltrials.models.enums import ResponseFormat, MarkupFormat
from clinicaltrials.models.fields import StudyField


class GetStudyInput(BaseModel):
    """Input parameters for the GET /studies/{nctId} endpoint."""
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra="forbid",
    )

    nct_id: str = Field(
        ...,
        description="NCT identifier for the clinical study (e.g., 'NCT00000102'). Must start with 'NCT' followed by digits.",
        pattern=r"^NCT\d+$",
    )
    format: ResponseFormat = Field(
        default=ResponseFormat.JSON,
        description="Response format: 'json' (default) for structured data or 'csv' for tabular output.",
    )
    markup_format: MarkupFormat = Field(
        default=MarkupFormat.MARKDOWN,
        description="Markup format for text fields: 'markdown' (default) or 'legacy'.",
    )
    fields: Optional[List[StudyField]] = Field(
        default=None,
        description=(
            "Specific fields to include in the response. "
            "If omitted, all fields are returned. "
            "Example: [NCTId, BriefTitle, OverallStatus, Phase]."
        ),
    )

    @field_validator("nct_id")
    @classmethod
    def normalize_nct_id(cls, v: str) -> str:
        return v.upper()
