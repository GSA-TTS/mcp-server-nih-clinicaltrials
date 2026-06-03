from typing import Optional
from pydantic import Field

from clinicaltrials.models.search import StudySearchBase


class SearchDatatableInput(StudySearchBase):
    """Input parameters for the search datatable tool."""

    # --- Sorting ---
    sort: Optional[str] = Field(
        default=None,
        description=(
            "Sort order as 'field:direction'. Direction is 'asc' or 'desc'. "
            "Example: 'LastUpdatePostDate:desc'."
        ),
    )
