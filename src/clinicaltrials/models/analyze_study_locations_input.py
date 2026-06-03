from pydantic import Field

from clinicaltrials.models.search import StudyQueryParams


class AnalyzeStudyLocationsInput(StudyQueryParams):
    """Input parameters for the study location analysis tool."""

    # --- Analysis target ---
    target_country: str = Field(
        default="United States",
        description=(
            "Country to use as the reference for location analysis. "
            "Defaults to 'United States'. Comparison is case-insensitive."
        ),
    )
