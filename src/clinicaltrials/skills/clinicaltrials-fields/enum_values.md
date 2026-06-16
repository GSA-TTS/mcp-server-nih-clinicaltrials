# Enumerated Parameter Values

Accepted values for enumerated parameters used by the ClinicalTrials.gov
MCP server tools (e.g. `filter_overall_status`, `agg_filter_phase`,
`agg_filter_study_type`). Pass values exactly as listed below.

## ResponseFormat

Response format for ClinicalTrials.gov API calls.

Accepted values: `json`, `csv`

## MarkupFormat

Markup format for text fields in ClinicalTrials.gov API responses.

Accepted values: `markdown`, `legacy`

## OverallStatus

Overall recruitment status of a clinical study.

Accepted values: `ACTIVE_NOT_RECRUITING`, `COMPLETED`, `ENROLLING_BY_INVITATION`, `NOT_YET_RECRUITING`, `RECRUITING`, `SUSPENDED`, `TERMINATED`, `WITHDRAWN`, `AVAILABLE`, `NO_LONGER_AVAILABLE`, `TEMPORARILY_NOT_AVAILABLE`, `APPROVED_FOR_MARKETING`, `WITHHELD`, `UNKNOWN`

## StudyType

Type of clinical study.

Accepted values: `EXPANDED_ACCESS`, `INTERVENTIONAL`, `OBSERVATIONAL`

## Phase

Phase of a clinical study.

Accepted values: `NA`, `EARLY_PHASE1`, `PHASE1`, `PHASE2`, `PHASE3`, `PHASE4`

## Sex

Sex/gender eligibility for a clinical study.

Accepted values: `FEMALE`, `MALE`, `ALL`

## StandardAge

Standardized age group for study eligibility.

Accepted values: `CHILD`, `ADULT`, `OLDER_ADULT`

## SamplingMethod

Sampling method used in an observational study.

Accepted values: `PROBABILITY_SAMPLE`, `NON_PROBABILITY_SAMPLE`

## IpdSharing

Whether individual participant data (IPD) will be shared.

Accepted values: `YES`, `NO`, `UNDECIDED`

## IpdSharingInfoType

Type of IPD sharing document available.

Accepted values: `STUDY_PROTOCOL`, `SAP`, `ICF`, `CSR`, `ANALYTIC_CODE`

## OrgStudyIdType

Type of organization study ID.

Accepted values: `NIH`, `FDA`, `VA`, `CDC`, `AHRQ`, `SAMHSA`

## SecondaryIdType

Type of secondary study identifier.

Accepted values: `NIH`, `FDA`, `VA`, `CDC`, `AHRQ`, `SAMHSA`, `OTHER_GRANT`, `EUDRACT_NUMBER`, `CTIS`, `REGISTRY`, `OTHER`

## AgencyClass

Classification of a sponsor or collaborator agency.

Accepted values: `NIH`, `FED`, `OTHER_GOV`, `INDIV`, `INDUSTRY`, `NETWORK`, `AMBIG`, `OTHER`, `UNKNOWN`

## ExpandedAccessStatus

Recruitment status for an expanded access study.

Accepted values: `AVAILABLE`, `NO_LONGER_AVAILABLE`, `TEMPORARILY_NOT_AVAILABLE`, `APPROVED_FOR_MARKETING`

## DateType

Whether a date is actual or estimated.

Accepted values: `ACTUAL`, `ESTIMATED`

## ResponsiblePartyType

Type of responsible party for a study.

Accepted values: `SPONSOR`, `PRINCIPAL_INVESTIGATOR`, `SPONSOR_INVESTIGATOR`

## DesignAllocation

Method of participant allocation in a study design.

Accepted values: `RANDOMIZED`, `NON_RANDOMIZED`, `NA`

## InterventionalAssignment

Assignment model for an interventional study.

Accepted values: `SINGLE_GROUP`, `PARALLEL`, `CROSSOVER`, `FACTORIAL`, `SEQUENTIAL`

## PrimaryPurpose

Primary purpose of a clinical study.

Accepted values: `TREATMENT`, `PREVENTION`, `DIAGNOSTIC`, `ECT`, `SUPPORTIVE_CARE`, `SCREENING`, `HEALTH_SERVICES_RESEARCH`, `BASIC_SCIENCE`, `DEVICE_FEASIBILITY`, `OTHER`

## ObservationalModel

Observational study model type.

Accepted values: `COHORT`, `CASE_CONTROL`, `CASE_ONLY`, `CASE_CROSSOVER`, `ECOLOGIC_OR_COMMUNITY`, `FAMILY_BASED`, `DEFINED_POPULATION`, `NATURAL_HISTORY`, `OTHER`

## DesignTimePerspective

Time perspective of an observational study.

Accepted values: `RETROSPECTIVE`, `PROSPECTIVE`, `CROSS_SECTIONAL`, `OTHER`

## BioSpecRetention

Whether and what type of biospecimens are retained.

Accepted values: `NONE_RETAINED`, `SAMPLES_WITH_DNA`, `SAMPLES_WITHOUT_DNA`

## EnrollmentType

Whether enrollment count is actual or estimated.

Accepted values: `ACTUAL`, `ESTIMATED`

## ArmGroupType

Type of arm or group in a clinical study.

Accepted values: `EXPERIMENTAL`, `ACTIVE_COMPARATOR`, `PLACEBO_COMPARATOR`, `SHAM_COMPARATOR`, `NO_INTERVENTION`, `OTHER`

## InterventionType

Type of intervention used in a clinical study.

Accepted values: `BEHAVIORAL`, `BIOLOGICAL`, `COMBINATION_PRODUCT`, `DEVICE`, `DIAGNOSTIC_TEST`, `DIETARY_SUPPLEMENT`, `DRUG`, `GENETIC`, `PROCEDURE`, `RADIATION`, `OTHER`

## ContactRole

Role of a study contact or location contact.

Accepted values: `STUDY_CHAIR`, `STUDY_DIRECTOR`, `PRINCIPAL_INVESTIGATOR`, `SUB_INVESTIGATOR`, `CONTACT`

## OfficialRole

Role of an overall official on a study.

Accepted values: `STUDY_CHAIR`, `STUDY_DIRECTOR`, `PRINCIPAL_INVESTIGATOR`, `SUB_INVESTIGATOR`

## RecruitmentStatus

Recruitment status at an individual study location.

Accepted values: `ACTIVE_NOT_RECRUITING`, `COMPLETED`, `ENROLLING_BY_INVITATION`, `NOT_YET_RECRUITING`, `RECRUITING`, `SUSPENDED`, `TERMINATED`, `WITHDRAWN`, `AVAILABLE`

## ReferenceType

Type of study reference citation.

Accepted values: `BACKGROUND`, `RESULT`, `DERIVED`

## MeasureParam

Statistical parameter type for an outcome or baseline measure.

Accepted values: `GEOMETRIC_MEAN`, `GEOMETRIC_LEAST_SQUARES_MEAN`, `LEAST_SQUARES_MEAN`, `LOG_MEAN`, `MEAN`, `MEDIAN`, `NUMBER`, `COUNT_OF_PARTICIPANTS`, `COUNT_OF_UNITS`

## MeasureDispersionType

Dispersion or precision type for an outcome or baseline measure.

Accepted values: `NA`, `STANDARD_DEVIATION`, `STANDARD_ERROR`, `INTER_QUARTILE_RANGE`, `FULL_RANGE`, `CONFIDENCE_80`, `CONFIDENCE_90`, `CONFIDENCE_95`, `CONFIDENCE_975`, `CONFIDENCE_99`, `CONFIDENCE_OTHER`, `GEOMETRIC_COEFFICIENT`

## OutcomeMeasureType

Classification of an outcome measure.

Accepted values: `PRIMARY`, `SECONDARY`, `OTHER_PRE_SPECIFIED`, `POST_HOC`

## ReportingStatus

Whether results for an outcome measure have been posted.

Accepted values: `NOT_POSTED`, `POSTED`

## EventAssessment

Collection approach for adverse event assessment.

Accepted values: `NON_SYSTEMATIC_ASSESSMENT`, `SYSTEMATIC_ASSESSMENT`

## AgreementRestrictionType

Type of publication restriction in a PI/sponsor agreement.

Accepted values: `LTE60`, `GT60`, `OTHER`

## BrowseLeafRelevance

Relevance of a MeSH browse leaf term to the study.

Accepted values: `LOW`, `HIGH`

## DesignMasking

Masking (blinding) type used in a study design.

Accepted values: `NONE`, `SINGLE`, `DOUBLE`, `TRIPLE`, `QUADRUPLE`

## WhoMasked

Which parties are masked in a study.

Accepted values: `PARTICIPANT`, `CARE_PROVIDER`, `INVESTIGATOR`, `OUTCOMES_ASSESSOR`

## AnalysisDispersionType

Dispersion type for a statistical analysis estimate.

Accepted values: `STANDARD_DEVIATION`, `STANDARD_ERROR_OF_MEAN`

## ConfidenceIntervalNumSides

Number of sides for a confidence interval.

Accepted values: `ONE_SIDED`, `TWO_SIDED`

## NonInferiorityType

Type of non-inferiority or superiority statistical test.

Accepted values: `SUPERIORITY`, `NON_INFERIORITY`, `EQUIVALENCE`, `OTHER`, `NON_INFERIORITY_OR_EQUIVALENCE`, `SUPERIORITY_OR_OTHER`, `NON_INFERIORITY_OR_EQUIVALENCE_LEGACY`, `SUPERIORITY_OR_OTHER_LEGACY`

## UnpostedEventType

Type of unposted results submission event.

Accepted values: `RESET`, `RELEASE`, `UNRELEASE`

## ViolationEventType

Type of FDA violation event.

Accepted values: `VIOLATION_IDENTIFIED`, `CORRECTION_CONFIRMED`, `PENALTY_IMPOSED`, `ISSUES_IN_LETTER_ADDRESSED_CONFIRMED`
