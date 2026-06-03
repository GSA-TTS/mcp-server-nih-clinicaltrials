from typing import Optional, List
from pydantic import Field

from clinicaltrials.models.search import StudySearchBase
from clinicaltrials.models.enums import ResponseFormat, MarkupFormat
from clinicaltrials.models.fields import StudyField, DEFAULT_SEARCH_FIELDS


class SearchStudiesInput(StudySearchBase):
    """Input parameters for the GET /studies (search) endpoint."""

    # --- Sorting & pagination ---
    sort: Optional[str] = Field(
        default=None,
        description=(
            "Sort order as 'field:direction'. Direction is 'asc' or 'desc'. "
            "Common sort fields: 'LastUpdatePostDate', 'StudyFirstPostDate', 'EnrollmentCount'. "
            "Example: 'LastUpdatePostDate:desc'."
        ),
    )
    page_size: int = Field(
        default=20,
        ge=1,
        le=1000,
        description="Number of studies to return per page (1–1000, default 20).",
    )
    page_token: Optional[str] = Field(
        default=None,
        description=(
            "Pagination cursor returned as 'nextPageToken' in a previous response. "
            "Pass this to retrieve the next page of results."
        ),
    )
    count_total: bool = Field(
        default=False,
        description="If true, include the total number of matching studies in the response.",
    )

    # --- Output format ---
    format: ResponseFormat = Field(
        default=ResponseFormat.JSON,
        description="Response format: 'json' (default) for structured data or 'csv' for tabular output.",
    )
    markup_format: MarkupFormat = Field(
        default=MarkupFormat.MARKDOWN,
        description="Markup format for text fields: 'markdown' (default) or 'legacy'.",
    )
    fields: Optional[List[StudyField]] = Field(
        default_factory=lambda: DEFAULT_SEARCH_FIELDS.copy(),
        description=(
            "Specific fields to return. Defaults to 19 essential fields "
            "(NCTId, BriefTitle, OverallStatus, Phase, Condition, InterventionName, etc.) "
            "to minimize context window usage. "
            "For comprehensive details on a single study, use clinicaltrials_get_study instead. "
            "Custom field list example: [NCTId, BriefTitle, Phase, EnrollmentCount]."
        ),
    )
