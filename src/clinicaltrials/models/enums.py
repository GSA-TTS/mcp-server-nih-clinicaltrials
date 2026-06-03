from enum import Enum


class ResponseFormat(str, Enum):
    """Response format for ClinicalTrials.gov API calls."""
    JSON = "json"
    CSV = "csv"


class MarkupFormat(str, Enum):
    """Markup format for text fields in ClinicalTrials.gov API responses."""
    MARKDOWN = "markdown"
    LEGACY = "legacy"


class OverallStatus(str, Enum):
    """Overall recruitment status of a clinical study."""
    ACTIVE_NOT_RECRUITING = "ACTIVE_NOT_RECRUITING"
    COMPLETED = "COMPLETED"
    ENROLLING_BY_INVITATION = "ENROLLING_BY_INVITATION"
    NOT_YET_RECRUITING = "NOT_YET_RECRUITING"
    RECRUITING = "RECRUITING"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"
    WITHDRAWN = "WITHDRAWN"
    AVAILABLE = "AVAILABLE"
    NO_LONGER_AVAILABLE = "NO_LONGER_AVAILABLE"
    TEMPORARILY_NOT_AVAILABLE = "TEMPORARILY_NOT_AVAILABLE"
    APPROVED_FOR_MARKETING = "APPROVED_FOR_MARKETING"
    WITHHELD = "WITHHELD"
    UNKNOWN = "UNKNOWN"


class StudyType(str, Enum):
    """Type of clinical study."""
    EXPANDED_ACCESS = "EXPANDED_ACCESS"
    INTERVENTIONAL = "INTERVENTIONAL"
    OBSERVATIONAL = "OBSERVATIONAL"


class Phase(str, Enum):
    """Phase of a clinical study."""
    NA = "NA"
    EARLY_PHASE1 = "EARLY_PHASE1"
    PHASE1 = "PHASE1"
    PHASE2 = "PHASE2"
    PHASE3 = "PHASE3"
    PHASE4 = "PHASE4"


class Sex(str, Enum):
    """Sex/gender eligibility for a clinical study."""
    FEMALE = "FEMALE"
    MALE = "MALE"
    ALL = "ALL"


class StandardAge(str, Enum):
    """Standardized age group for study eligibility."""
    CHILD = "CHILD"
    ADULT = "ADULT"
    OLDER_ADULT = "OLDER_ADULT"


class SamplingMethod(str, Enum):
    """Sampling method used in an observational study."""
    PROBABILITY_SAMPLE = "PROBABILITY_SAMPLE"
    NON_PROBABILITY_SAMPLE = "NON_PROBABILITY_SAMPLE"


class IpdSharing(str, Enum):
    """Whether individual participant data (IPD) will be shared."""
    YES = "YES"
    NO = "NO"
    UNDECIDED = "UNDECIDED"


class IpdSharingInfoType(str, Enum):
    """Type of IPD sharing document available."""
    STUDY_PROTOCOL = "STUDY_PROTOCOL"
    SAP = "SAP"
    ICF = "ICF"
    CSR = "CSR"
    ANALYTIC_CODE = "ANALYTIC_CODE"


class OrgStudyIdType(str, Enum):
    """Type of organization study ID."""
    NIH = "NIH"
    FDA = "FDA"
    VA = "VA"
    CDC = "CDC"
    AHRQ = "AHRQ"
    SAMHSA = "SAMHSA"


class SecondaryIdType(str, Enum):
    """Type of secondary study identifier."""
    NIH = "NIH"
    FDA = "FDA"
    VA = "VA"
    CDC = "CDC"
    AHRQ = "AHRQ"
    SAMHSA = "SAMHSA"
    OTHER_GRANT = "OTHER_GRANT"
    EUDRACT_NUMBER = "EUDRACT_NUMBER"
    CTIS = "CTIS"
    REGISTRY = "REGISTRY"
    OTHER = "OTHER"


class AgencyClass(str, Enum):
    """Classification of a sponsor or collaborator agency."""
    NIH = "NIH"
    FED = "FED"
    OTHER_GOV = "OTHER_GOV"
    INDIV = "INDIV"
    INDUSTRY = "INDUSTRY"
    NETWORK = "NETWORK"
    AMBIG = "AMBIG"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"


class ExpandedAccessStatus(str, Enum):
    """Recruitment status for an expanded access study."""
    AVAILABLE = "AVAILABLE"
    NO_LONGER_AVAILABLE = "NO_LONGER_AVAILABLE"
    TEMPORARILY_NOT_AVAILABLE = "TEMPORARILY_NOT_AVAILABLE"
    APPROVED_FOR_MARKETING = "APPROVED_FOR_MARKETING"


class DateType(str, Enum):
    """Whether a date is actual or estimated."""
    ACTUAL = "ACTUAL"
    ESTIMATED = "ESTIMATED"


class ResponsiblePartyType(str, Enum):
    """Type of responsible party for a study."""
    SPONSOR = "SPONSOR"
    PRINCIPAL_INVESTIGATOR = "PRINCIPAL_INVESTIGATOR"
    SPONSOR_INVESTIGATOR = "SPONSOR_INVESTIGATOR"


class DesignAllocation(str, Enum):
    """Method of participant allocation in a study design."""
    RANDOMIZED = "RANDOMIZED"
    NON_RANDOMIZED = "NON_RANDOMIZED"
    NA = "NA"


class InterventionalAssignment(str, Enum):
    """Assignment model for an interventional study."""
    SINGLE_GROUP = "SINGLE_GROUP"
    PARALLEL = "PARALLEL"
    CROSSOVER = "CROSSOVER"
    FACTORIAL = "FACTORIAL"
    SEQUENTIAL = "SEQUENTIAL"


class PrimaryPurpose(str, Enum):
    """Primary purpose of a clinical study."""
    TREATMENT = "TREATMENT"
    PREVENTION = "PREVENTION"
    DIAGNOSTIC = "DIAGNOSTIC"
    ECT = "ECT"
    SUPPORTIVE_CARE = "SUPPORTIVE_CARE"
    SCREENING = "SCREENING"
    HEALTH_SERVICES_RESEARCH = "HEALTH_SERVICES_RESEARCH"
    BASIC_SCIENCE = "BASIC_SCIENCE"
    DEVICE_FEASIBILITY = "DEVICE_FEASIBILITY"
    OTHER = "OTHER"


class ObservationalModel(str, Enum):
    """Observational study model type."""
    COHORT = "COHORT"
    CASE_CONTROL = "CASE_CONTROL"
    CASE_ONLY = "CASE_ONLY"
    CASE_CROSSOVER = "CASE_CROSSOVER"
    ECOLOGIC_OR_COMMUNITY = "ECOLOGIC_OR_COMMUNITY"
    FAMILY_BASED = "FAMILY_BASED"
    DEFINED_POPULATION = "DEFINED_POPULATION"
    NATURAL_HISTORY = "NATURAL_HISTORY"
    OTHER = "OTHER"


class DesignTimePerspective(str, Enum):
    """Time perspective of an observational study."""
    RETROSPECTIVE = "RETROSPECTIVE"
    PROSPECTIVE = "PROSPECTIVE"
    CROSS_SECTIONAL = "CROSS_SECTIONAL"
    OTHER = "OTHER"


class BioSpecRetention(str, Enum):
    """Whether and what type of biospecimens are retained."""
    NONE_RETAINED = "NONE_RETAINED"
    SAMPLES_WITH_DNA = "SAMPLES_WITH_DNA"
    SAMPLES_WITHOUT_DNA = "SAMPLES_WITHOUT_DNA"


class EnrollmentType(str, Enum):
    """Whether enrollment count is actual or estimated."""
    ACTUAL = "ACTUAL"
    ESTIMATED = "ESTIMATED"


class ArmGroupType(str, Enum):
    """Type of arm or group in a clinical study."""
    EXPERIMENTAL = "EXPERIMENTAL"
    ACTIVE_COMPARATOR = "ACTIVE_COMPARATOR"
    PLACEBO_COMPARATOR = "PLACEBO_COMPARATOR"
    SHAM_COMPARATOR = "SHAM_COMPARATOR"
    NO_INTERVENTION = "NO_INTERVENTION"
    OTHER = "OTHER"


class InterventionType(str, Enum):
    """Type of intervention used in a clinical study."""
    BEHAVIORAL = "BEHAVIORAL"
    BIOLOGICAL = "BIOLOGICAL"
    COMBINATION_PRODUCT = "COMBINATION_PRODUCT"
    DEVICE = "DEVICE"
    DIAGNOSTIC_TEST = "DIAGNOSTIC_TEST"
    DIETARY_SUPPLEMENT = "DIETARY_SUPPLEMENT"
    DRUG = "DRUG"
    GENETIC = "GENETIC"
    PROCEDURE = "PROCEDURE"
    RADIATION = "RADIATION"
    OTHER = "OTHER"


class ContactRole(str, Enum):
    """Role of a study contact or location contact."""
    STUDY_CHAIR = "STUDY_CHAIR"
    STUDY_DIRECTOR = "STUDY_DIRECTOR"
    PRINCIPAL_INVESTIGATOR = "PRINCIPAL_INVESTIGATOR"
    SUB_INVESTIGATOR = "SUB_INVESTIGATOR"
    CONTACT = "CONTACT"


class OfficialRole(str, Enum):
    """Role of an overall official on a study."""
    STUDY_CHAIR = "STUDY_CHAIR"
    STUDY_DIRECTOR = "STUDY_DIRECTOR"
    PRINCIPAL_INVESTIGATOR = "PRINCIPAL_INVESTIGATOR"
    SUB_INVESTIGATOR = "SUB_INVESTIGATOR"


class RecruitmentStatus(str, Enum):
    """Recruitment status at an individual study location."""
    ACTIVE_NOT_RECRUITING = "ACTIVE_NOT_RECRUITING"
    COMPLETED = "COMPLETED"
    ENROLLING_BY_INVITATION = "ENROLLING_BY_INVITATION"
    NOT_YET_RECRUITING = "NOT_YET_RECRUITING"
    RECRUITING = "RECRUITING"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"
    WITHDRAWN = "WITHDRAWN"
    AVAILABLE = "AVAILABLE"


class ReferenceType(str, Enum):
    """Type of study reference citation."""
    BACKGROUND = "BACKGROUND"
    RESULT = "RESULT"
    DERIVED = "DERIVED"


class MeasureParam(str, Enum):
    """Statistical parameter type for an outcome or baseline measure."""
    GEOMETRIC_MEAN = "GEOMETRIC_MEAN"
    GEOMETRIC_LEAST_SQUARES_MEAN = "GEOMETRIC_LEAST_SQUARES_MEAN"
    LEAST_SQUARES_MEAN = "LEAST_SQUARES_MEAN"
    LOG_MEAN = "LOG_MEAN"
    MEAN = "MEAN"
    MEDIAN = "MEDIAN"
    NUMBER = "NUMBER"
    COUNT_OF_PARTICIPANTS = "COUNT_OF_PARTICIPANTS"
    COUNT_OF_UNITS = "COUNT_OF_UNITS"


class MeasureDispersionType(str, Enum):
    """Dispersion or precision type for an outcome or baseline measure."""
    NA = "NA"
    STANDARD_DEVIATION = "STANDARD_DEVIATION"
    STANDARD_ERROR = "STANDARD_ERROR"
    INTER_QUARTILE_RANGE = "INTER_QUARTILE_RANGE"
    FULL_RANGE = "FULL_RANGE"
    CONFIDENCE_80 = "CONFIDENCE_80"
    CONFIDENCE_90 = "CONFIDENCE_90"
    CONFIDENCE_95 = "CONFIDENCE_95"
    CONFIDENCE_975 = "CONFIDENCE_975"
    CONFIDENCE_99 = "CONFIDENCE_99"
    CONFIDENCE_OTHER = "CONFIDENCE_OTHER"
    GEOMETRIC_COEFFICIENT = "GEOMETRIC_COEFFICIENT"


class OutcomeMeasureType(str, Enum):
    """Classification of an outcome measure."""
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    OTHER_PRE_SPECIFIED = "OTHER_PRE_SPECIFIED"
    POST_HOC = "POST_HOC"


class ReportingStatus(str, Enum):
    """Whether results for an outcome measure have been posted."""
    NOT_POSTED = "NOT_POSTED"
    POSTED = "POSTED"


class EventAssessment(str, Enum):
    """Collection approach for adverse event assessment."""
    NON_SYSTEMATIC_ASSESSMENT = "NON_SYSTEMATIC_ASSESSMENT"
    SYSTEMATIC_ASSESSMENT = "SYSTEMATIC_ASSESSMENT"


class AgreementRestrictionType(str, Enum):
    """Type of publication restriction in a PI/sponsor agreement."""
    LTE60 = "LTE60"
    GT60 = "GT60"
    OTHER = "OTHER"


class BrowseLeafRelevance(str, Enum):
    """Relevance of a MeSH browse leaf term to the study."""
    LOW = "LOW"
    HIGH = "HIGH"


class DesignMasking(str, Enum):
    """Masking (blinding) type used in a study design."""
    NONE = "NONE"
    SINGLE = "SINGLE"
    DOUBLE = "DOUBLE"
    TRIPLE = "TRIPLE"
    QUADRUPLE = "QUADRUPLE"


class WhoMasked(str, Enum):
    """Which parties are masked in a study."""
    PARTICIPANT = "PARTICIPANT"
    CARE_PROVIDER = "CARE_PROVIDER"
    INVESTIGATOR = "INVESTIGATOR"
    OUTCOMES_ASSESSOR = "OUTCOMES_ASSESSOR"


class AnalysisDispersionType(str, Enum):
    """Dispersion type for a statistical analysis estimate."""
    STANDARD_DEVIATION = "STANDARD_DEVIATION"
    STANDARD_ERROR_OF_MEAN = "STANDARD_ERROR_OF_MEAN"


class ConfidenceIntervalNumSides(str, Enum):
    """Number of sides for a confidence interval."""
    ONE_SIDED = "ONE_SIDED"
    TWO_SIDED = "TWO_SIDED"


class NonInferiorityType(str, Enum):
    """Type of non-inferiority or superiority statistical test."""
    SUPERIORITY = "SUPERIORITY"
    NON_INFERIORITY = "NON_INFERIORITY"
    EQUIVALENCE = "EQUIVALENCE"
    OTHER = "OTHER"
    NON_INFERIORITY_OR_EQUIVALENCE = "NON_INFERIORITY_OR_EQUIVALENCE"
    SUPERIORITY_OR_OTHER = "SUPERIORITY_OR_OTHER"
    NON_INFERIORITY_OR_EQUIVALENCE_LEGACY = "NON_INFERIORITY_OR_EQUIVALENCE_LEGACY"
    SUPERIORITY_OR_OTHER_LEGACY = "SUPERIORITY_OR_OTHER_LEGACY"


class UnpostedEventType(str, Enum):
    """Type of unposted results submission event."""
    RESET = "RESET"
    RELEASE = "RELEASE"
    UNRELEASE = "UNRELEASE"


class ViolationEventType(str, Enum):
    """Type of FDA violation event."""
    VIOLATION_IDENTIFIED = "VIOLATION_IDENTIFIED"
    CORRECTION_CONFIRMED = "CORRECTION_CONFIRMED"
    PENALTY_IMPOSED = "PENALTY_IMPOSED"
    ISSUES_IN_LETTER_ADDRESSED_CONFIRMED = "ISSUES_IN_LETTER_ADDRESSED_CONFIRMED"
