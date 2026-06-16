from typing import Optional, List
from pydantic import BaseModel, Field, field_validator, ConfigDict

from clinicaltrials.models.enums import ResponseFormat, MarkupFormat
from clinicaltrials.models.fields import (
    STUDY_FIELDS_SKILL_RESOURCE,
    validate_study_fields,
)


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
    fields: Optional[List[str]] = Field(
        default=None,
        description=(
            "Study field names to include in the response. If omitted, all fields "
            "are returned. For the full list of valid field names, read the resource "
            f"{STUDY_FIELDS_SKILL_RESOURCE}."
        ),
    )

    @field_validator("nct_id")
    @classmethod
    def normalize_nct_id(cls, v: str) -> str:
        return v.upper()

    @field_validator("fields")
    @classmethod
    def _validate_fields(cls, v):
        if v is None:
            return v
        return validate_study_fields(v)
