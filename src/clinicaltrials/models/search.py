from typing import Optional, List
from pydantic import BaseModel, Field, model_validator, ConfigDict

from clinicaltrials.models.enums import OverallStatus, Phase, StudyType


_PHASE_AGG: dict = {
    Phase.NA: "na",
    Phase.EARLY_PHASE1: "0",
    Phase.PHASE1: "1",
    Phase.PHASE2: "2",
    Phase.PHASE3: "3",
    Phase.PHASE4: "4",
}

_STUDY_TYPE_AGG: dict = {
    StudyType.INTERVENTIONAL: "int",
    StudyType.OBSERVATIONAL: "obs",
    StudyType.EXPANDED_ACCESS: "exp",
}


class StudyQueryParams(BaseModel):
    """Shared query and filter parameters for clinical study search endpoints."""
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra="forbid",
    )

    # --- Query parameters ---
    query_cond: Optional[str] = Field(
        default=None,
        description="Search by condition or disease (e.g., 'diabetes', 'breast cancer').",
    )
    query_term: Optional[str] = Field(
        default=None,
        description=(
            "General keyword search across all study fields (e.g., 'mRNA vaccine'). "
            "Also matches enum-typed fields when exact enum values are provided — "
            "use values from the corresponding enum classes for precise matching: "
            "Phase (e.g., 'PHASE2'), StandardAge (e.g., 'ADULT'), "
            "StudyType (e.g., 'INTERVENTIONAL'), InterventionType (e.g., 'DRUG'), "
            "ArmGroupType (e.g., 'EXPERIMENTAL'), RecruitmentStatus / LocationStatus (e.g., 'RECRUITING'), "
            "DesignAllocation (e.g., 'RANDOMIZED'), InterventionalAssignment (e.g., 'PARALLEL'), "
            "DesignMasking (e.g., 'DOUBLE'), WhoMasked (e.g., 'PARTICIPANT'), "
            "ObservationalModel (e.g., 'COHORT'), PrimaryPurpose (e.g., 'TREATMENT'), "
            "DesignTimePerspective (e.g., 'PROSPECTIVE')."
        ),
    )
    query_intr: Optional[str] = Field(
        default=None,
        description=(
            "Search by intervention or treatment name (e.g., 'insulin', 'pembrolizumab'). "
            "Also matches enum-typed fields when exact enum values are provided: "
            "InterventionType (e.g., 'DRUG', 'BIOLOGICAL', 'DEVICE'), "
            "ArmGroupType (e.g., 'EXPERIMENTAL', 'PLACEBO_COMPARATOR')."
        ),
    )
    query_titles: Optional[str] = Field(
        default=None,
        description="Search within study titles only (e.g., 'long COVID fatigue').",
    )
    query_id: Optional[str] = Field(
        default=None,
        description="Search by study ID, including NCT IDs and other secondary identifiers.",
    )
    query_spons: Optional[str] = Field(
        default=None,
        description="Search by sponsor or collaborator name (e.g., 'NIH', 'Pfizer').",
    )
    query_locn: Optional[str] = Field(
        default=None,
        description=(
            "Search by location terms such as facility name, city, state, or country. "
            "Supports simple text search (e.g., 'Boston', 'Mayo Clinic') or AREA syntax for field-specific queries. "
            "AREA syntax examples: 'AREA[LocationState]MA', 'AREA[LocationCountry]US', 'AREA[LocationCity]Boston'. "
            "Available fields: LocationCity, LocationState, LocationCountry, LocationFacility, LocationZip."
        ),
    )
    query_patient: Optional[str] = Field(
        default=None,
        description=(
            "Patient-friendly search using plain language (e.g., 'cancer survivor exercise program'). "
            "Also matches enum-typed fields when exact enum values are provided: "
            "StandardAge (e.g., 'CHILD', 'ADULT', 'OLDER_ADULT'), "
            "InterventionalAssignment (e.g., 'PARALLEL', 'CROSSOVER'), "
            "DesignMasking (e.g., 'DOUBLE', 'TRIPLE'), "
            "WhoMasked (e.g., 'PARTICIPANT', 'INVESTIGATOR'), "
            "ObservationalModel (e.g., 'COHORT', 'CASE_CONTROL'), "
            "PrimaryPurpose (e.g., 'TREATMENT', 'PREVENTION'), "
            "DesignTimePerspective (e.g., 'PROSPECTIVE', 'RETROSPECTIVE')."
        ),
    )

    # --- Filters ---
    filter_overall_status: Optional[List[OverallStatus]] = Field(
        default=None,
        description=(
            "Filter by recruitment status. Accepted values: RECRUITING, NOT_YET_RECRUITING, "
            "ACTIVE_NOT_RECRUITING, COMPLETED, ENROLLING_BY_INVITATION, TERMINATED, "
            "WITHDRAWN, SUSPENDED, UNKNOWN."
        ),
    )
    filter_geo: Optional[str] = Field(
        default=None,
        description=(
            "Filter studies to those with a location within a geographic radius. "
            "Format: 'distance(lat,lon,radius)' where radius uses 'mi' or 'km' "
            "(e.g., 'distance(39.0,-77.0,50mi)')."
        ),
    )
    filter_ids: Optional[List[str]] = Field(
        default=None,
        description="Filter to a specific list of NCT IDs (e.g., ['NCT04280705', 'NCT00000102']).",
    )
    filter_advanced: Optional[str] = Field(
        default=None,
        description=(
            "Filter by query in Essie expression syntax."
            "Prefer using the typed filter fields (e.g., filter_overall_status, filter_geo, agg_filter_phase) when possible, "
            "but this allows for advanced users to specify any valid Essie filter expression as a raw string. "
            "Example: AREA[StartDate]2022 | AREA[CompletionDate]2022-12-01 ┃ AREA[MinimumAge]RANGE[MIN, 16 years] AND AREA[MaximumAge]RANGE[16 years, MAX]"
        )
    )
    post_filter_overall_status: Optional[List[OverallStatus]] = Field(
        default=None,
        description=(
            "Same as filter_overall_status but applied after aggregation counts are computed, "
            "so counts reflect the full result set rather than the filtered subset."
        ),
    )
    post_filter_geo: Optional[str] = Field(
        default=None,
        description=(
            "Same as filter_geo but applied after aggregation counts are computed. "
            "Format: 'distance(lat,lon,radius)' (e.g., 'distance(42.36,-71.06,25mi)')."
        ),
    )
    agg_filter_phase: Optional[List[Phase]] = Field(
        default=None,
        description=(
            "Filter by study phase. Accepts one or more Phase values: "
            "NA, EARLY_PHASE1, PHASE1, PHASE2, PHASE3, PHASE4. "
            "Example: [PHASE2, PHASE3]. Cannot be combined with agg_filters."
        ),
    )
    agg_filter_study_type: Optional[List[StudyType]] = Field(
        default=None,
        description=(
            "Filter by study type. Accepts one or more StudyType values: "
            "INTERVENTIONAL, OBSERVATIONAL, EXPANDED_ACCESS. "
            "Example: [INTERVENTIONAL]. Cannot be combined with agg_filters."
        ),
    )
    agg_filters: Optional[str] = Field(
        default=None,
        description=(
            "Raw aggregation filter string for advanced use. "
            "Prefer agg_filter_phase and agg_filter_study_type when possible. "
            "Cannot be combined with those typed fields. "
            "Phase tokens: '0' (early phase 1), '1', '2', '3', '4', 'na'. "
            "Study type tokens: 'int' (interventional), 'obs' (observational), 'exp' (expanded access). "
            "Example: 'phase:2 3,studyType:int'."
        ),
    )

    @model_validator(mode="after")
    def build_agg_filters(self) -> "StudyQueryParams":
        has_typed = self.agg_filter_phase or self.agg_filter_study_type
        if has_typed and self.agg_filters is not None:
            raise ValueError(
                "agg_filters cannot be combined with agg_filter_phase or agg_filter_study_type. "
                "Use the typed fields or the raw string, not both."
            )
        if has_typed:
            parts = []
            if self.agg_filter_phase:
                tokens = " ".join(_PHASE_AGG[p] for p in self.agg_filter_phase)
                parts.append(f"phase:{tokens}")
            if self.agg_filter_study_type:
                tokens = " ".join(_STUDY_TYPE_AGG[t] for t in self.agg_filter_study_type)
                parts.append(f"studyType:{tokens}")
            object.__setattr__(self, "agg_filters", ",".join(parts))
        return self


class StudySearchBase(StudyQueryParams):
    """Extends StudyQueryParams with a validator requiring at least one query or filter."""

    @model_validator(mode="after")
    def require_at_least_one_query_or_filter(self) -> "StudySearchBase":
        query_fields = [
            self.query_cond, self.query_term, self.query_intr, self.query_titles,
            self.query_id, self.query_spons, self.query_locn, self.query_patient,
            self.filter_ids, self.agg_filter_phase, self.agg_filter_study_type,
            self.agg_filters, self.filter_advanced
        ]
        if not any(query_fields):
            raise ValueError(
                "At least one query parameter (query_cond, query_term, query_intr, "
                "query_titles, query_id, query_spons, query_locn, query_patient), "
                "filter_ids, agg_filter_phase, agg_filter_study_type, or agg_filters "
                "must be provided."
            )
        return self
