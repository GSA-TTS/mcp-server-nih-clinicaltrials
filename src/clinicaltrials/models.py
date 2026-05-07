from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, Field, field_validator, model_validator, ConfigDict


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


class StudyField(str, Enum):
    """All valid field names for ClinicalTrials.gov study records.

    Use these values in the `fields` parameter to request specific data columns.
    Sourced from GET /studies/metadata.
    """
    # Identification
    NCTId = "NCTId"  # National Clinical Trial (NCT) Identification Number
    NCTIdAlias = "NCTIdAlias"  # Obsolete or duplicate NCT associated with a published NCT
    OrgStudyId = "OrgStudyId"  # Organization's Unique Protocol Identification Number
    OrgStudyIdType = "OrgStudyIdType"  # Organization ID Type
    OrgStudyIdLink = "OrgStudyIdLink"  # Organization ID Link
    SecondaryId = "SecondaryId"  # Secondary ID
    SecondaryIdType = "SecondaryIdType"  # Secondary ID Type
    SecondaryIdDomain = "SecondaryIdDomain"  # Secondary ID Description based on ID Type selected
    SecondaryIdLink = "SecondaryIdLink"  # Secondary ID Link
    BriefTitle = "BriefTitle"  # Brief Title
    OfficialTitle = "OfficialTitle"  # Official Title
    Acronym = "Acronym"  # Acronym
    OrgFullName = "OrgFullName"  # Organization Full Name
    OrgClass = "OrgClass"  # Organization type

    # Status
    StatusVerifiedDate = "StatusVerifiedDate"  # Record Verification Date
    OverallStatus = "OverallStatus"  # Overall Recruitment Status or Expanded Access Status
    LastKnownStatus = "LastKnownStatus"  # Last Known Status
    DelayedPosting = "DelayedPosting"  # Delayed Posting
    WhyStopped = "WhyStopped"  # Reason why a study stopped
    HasExpandedAccess = "HasExpandedAccess"  # Has EA for compassionate use
    ExpandedAccessNCTId = "ExpandedAccessNCTId"  # NCT of an EA study
    ExpandedAccessStatusForNCTId = "ExpandedAccessStatusForNCTId"  # EA Recruitment Status
    StartDate = "StartDate"  # Study Start Date
    StartDateType = "StartDateType"  # Study Start Date Type
    PrimaryCompletionDate = "PrimaryCompletionDate"  # Primary Completion Date
    PrimaryCompletionDateType = "PrimaryCompletionDateType"  # Primary Completion Date Type
    CompletionDate = "CompletionDate"  # Study Completion Date
    CompletionDateType = "CompletionDateType"  # Study Completion Date Type
    StudyFirstSubmitDate = "StudyFirstSubmitDate"  # Study First Submitted Date
    StudyFirstSubmitQCDate = "StudyFirstSubmitQCDate"  # Study First Submission Date that Met QC Criteria
    StudyFirstPostDate = "StudyFirstPostDate"  # Study First Posted Date
    StudyFirstPostDateType = "StudyFirstPostDateType"  # First Study Posted Date Type
    ResultsWaived = "ResultsWaived"  # Results Waived
    ResultsFirstSubmitDate = "ResultsFirstSubmitDate"  # Results First Submitted Date
    ResultsFirstSubmitQCDate = "ResultsFirstSubmitQCDate"  # Results First Submitted that Met QC Criteria
    ResultsFirstPostDate = "ResultsFirstPostDate"  # Results First Posted Date
    ResultsFirstPostDateType = "ResultsFirstPostDateType"  # Results First Posted Date Type
    DispFirstSubmitDate = "DispFirstSubmitDate"  # Certification/Extension First Submitted Date
    DispFirstSubmitQCDate = "DispFirstSubmitQCDate"  # Certification/Extension First Submitted that Passed QC Review
    DispFirstPostDate = "DispFirstPostDate"  # Certification/Extension First Posted Date
    DispFirstPostDateType = "DispFirstPostDateType"  # Certification/Extension First Posted Date Type
    LastUpdateSubmitDate = "LastUpdateSubmitDate"  # Last Update Submitted Date
    LastUpdatePostDate = "LastUpdatePostDate"  # Last Update Posted Date
    LastUpdatePostDateType = "LastUpdatePostDateType"  # Last Update Posted Date Type

    # Sponsor / Responsible Party
    ResponsiblePartyType = "ResponsiblePartyType"  # Responsible Party Type
    ResponsiblePartyInvestigatorFullName = "ResponsiblePartyInvestigatorFullName"  # Responsible Party Investigator Full Name
    ResponsiblePartyInvestigatorTitle = "ResponsiblePartyInvestigatorTitle"  # Responsible Party Investigator Title
    ResponsiblePartyInvestigatorAffiliation = "ResponsiblePartyInvestigatorAffiliation"  # Responsible Party Investigator Affiliation
    ResponsiblePartyOldNameTitle = "ResponsiblePartyOldNameTitle"  # Older format for Responsible Party Investigator Title
    ResponsiblePartyOldOrganization = "ResponsiblePartyOldOrganization"  # Older format for Responsible Party Investigator Organization
    LeadSponsorName = "LeadSponsorName"  # Lead Sponsor Name
    LeadSponsorClass = "LeadSponsorClass"  # Lead Sponsor Type
    CollaboratorName = "CollaboratorName"  # Collaborator Name
    CollaboratorClass = "CollaboratorClass"  # Collaborator Type

    # Oversight
    OversightHasDMC = "OversightHasDMC"  # Has Data Monitoring Committee (DMC)
    IsFDARegulatedDrug = "IsFDARegulatedDrug"  # Is FDA Regulated Drug
    IsFDARegulatedDevice = "IsFDARegulatedDevice"  # Is FDA Regulated Device
    IsUnapprovedDevice = "IsUnapprovedDevice"  # Is Unapproved Device
    IsPPSD = "IsPPSD"  # Pediatric Postmarket Surveillance of a Device Product
    IsUSExport = "IsUSExport"  # Product Exported from US
    FDAAA801Violation = "FDAAA801Violation"  # FDA AA 801 Violation

    # Description
    BriefSummary = "BriefSummary"  # Brief Summary
    DetailedDescription = "DetailedDescription"  # Detailed Description

    # Conditions / Keywords
    Condition = "Condition"  # Condition/Disease
    Keyword = "Keyword"  # Keyword

    # Design
    StudyType = "StudyType"  # Study Type
    NPtrsToThisExpAccNCTId = "NPtrsToThisExpAccNCTId"  # Number of References to an Expanded Access Study
    ExpAccTypeIndividual = "ExpAccTypeIndividual"  # Individual Patients
    ExpAccTypeIntermediate = "ExpAccTypeIntermediate"  # Intermediate-type Population
    ExpAccTypeTreatment = "ExpAccTypeTreatment"  # Treatment IND/Protocol
    PatientRegistry = "PatientRegistry"  # Patient Registry
    TargetDuration = "TargetDuration"  # Target Follow-Up Duration
    Phase = "Phase"  # Study Phase
    DesignAllocation = "DesignAllocation"  # Design Allocation
    DesignInterventionModel = "DesignInterventionModel"  # Interventional Study Design
    DesignInterventionModelDescription = "DesignInterventionModelDescription"  # Interventional Study Design Description
    DesignPrimaryPurpose = "DesignPrimaryPurpose"  # Design Primary Purpose
    DesignObservationalModel = "DesignObservationalModel"  # Observational Study Model
    DesignTimePerspective = "DesignTimePerspective"  # Time Perspective
    DesignMasking = "DesignMasking"  # Design Masking
    DesignMaskingDescription = "DesignMaskingDescription"  # Masking Description
    DesignWhoMasked = "DesignWhoMasked"  # Who is Masked
    BioSpecRetention = "BioSpecRetention"  # Biospecimen Retention
    BioSpecDescription = "BioSpecDescription"  # Biospecimen Description
    EnrollmentCount = "EnrollmentCount"  # Enrollment
    EnrollmentType = "EnrollmentType"  # Enrollment Type

    # Arms / Interventions
    ArmGroupLabel = "ArmGroupLabel"  # Arm Group Label
    ArmGroupType = "ArmGroupType"  # Arm Group Type
    ArmGroupDescription = "ArmGroupDescription"  # Arm Description for INT, Group/Cohort Description for OBS
    ArmGroupInterventionName = "ArmGroupInterventionName"  # Arm/Group that Receives a Specific Intervention
    InterventionType = "InterventionType"  # Intervention/Treatment Type
    InterventionName = "InterventionName"  # Intervention Name
    InterventionDescription = "InterventionDescription"  # Intervention Description
    InterventionArmGroupLabel = "InterventionArmGroupLabel"  # Arm Group Label for Intervention
    InterventionOtherName = "InterventionOtherName"  # Other Intervention Name

    # Outcomes
    PrimaryOutcomeMeasure = "PrimaryOutcomeMeasure"  # Primary Outcome Title
    PrimaryOutcomeDescription = "PrimaryOutcomeDescription"  # Primary Outcome Measure Description
    PrimaryOutcomeTimeFrame = "PrimaryOutcomeTimeFrame"  # Primary Outcome Measure Time Frame
    SecondaryOutcomeMeasure = "SecondaryOutcomeMeasure"  # Secondary Outcome Measure Title
    SecondaryOutcomeDescription = "SecondaryOutcomeDescription"  # Secondary Outcome Measure Description
    SecondaryOutcomeTimeFrame = "SecondaryOutcomeTimeFrame"  # Secondary Outcome Measure Time Frame
    OtherOutcomeMeasure = "OtherOutcomeMeasure"  # Other Outcome Measure Title
    OtherOutcomeDescription = "OtherOutcomeDescription"  # Other Outcome Measure Description
    OtherOutcomeTimeFrame = "OtherOutcomeTimeFrame"  # Other Outcome Measure Time Frame

    # Eligibility
    EligibilityCriteria = "EligibilityCriteria"  # Inclusion and exclusion eligibility criteria
    HealthyVolunteers = "HealthyVolunteers"  # Accepts Healthy Volunteers
    Sex = "Sex"  # Sex/Gender
    GenderBased = "GenderBased"  # Gender-Based Eligibility
    GenderDescription = "GenderDescription"  # Gender Description
    MinimumAge = "MinimumAge"  # Minimum Age
    MaximumAge = "MaximumAge"  # Maximum Age
    StdAge = "StdAge"  # Age Group
    StudyPopulation = "StudyPopulation"  # Study Population Description
    SamplingMethod = "SamplingMethod"  # Sampling Method

    # Contacts / Locations
    CentralContactName = "CentralContactName"  # Central Contact Name
    CentralContactRole = "CentralContactRole"  # Central Contact Role
    CentralContactPhone = "CentralContactPhone"  # Central Contact Phone
    CentralContactPhoneExt = "CentralContactPhoneExt"  # Central Contact Phone Ext
    CentralContactEMail = "CentralContactEMail"  # Central Contact EMail
    OverallOfficialName = "OverallOfficialName"  # Overall Official Name
    OverallOfficialAffiliation = "OverallOfficialAffiliation"  # Overall Official Affiliation
    OverallOfficialRole = "OverallOfficialRole"  # Overall Official Role
    LocationFacility = "LocationFacility"  # Facility Name
    LocationStatus = "LocationStatus"  # Individual site recruitment status
    LocationCity = "LocationCity"  # City
    LocationState = "LocationState"  # State
    LocationZip = "LocationZip"  # Zipcode
    LocationCountry = "LocationCountry"  # Country
    LocationContactName = "LocationContactName"  # Location Contact Name
    LocationContactRole = "LocationContactRole"  # Location Contact Role
    LocationContactPhone = "LocationContactPhone"  # Location Contact Phone
    LocationContactPhoneExt = "LocationContactPhoneExt"  # Location Contact Phone Ext
    LocationContactEMail = "LocationContactEMail"  # Location Contact EMail
    LocationGeoPoint = "LocationGeoPoint"  # Location Geo Point

    # References / Links
    ReferencePMID = "ReferencePMID"  # PubMed Identifier
    ReferenceType = "ReferenceType"  # Reference Type
    ReferenceCitation = "ReferenceCitation"  # Reference Citation
    RetractionPMID = "RetractionPMID"  # PMID for Publication Retraction
    RetractionSource = "RetractionSource"  # Retraction Source
    SeeAlsoLinkLabel = "SeeAlsoLinkLabel"  # See Also Link Label Title
    SeeAlsoLinkURL = "SeeAlsoLinkURL"  # See Also Link URL

    # IPD Sharing
    AvailIPDId = "AvailIPDId"  # Available IPD ID
    AvailIPDType = "AvailIPDType"  # Available IPD Type
    AvailIPDURL = "AvailIPDURL"  # Available IPD URL
    AvailIPDComment = "AvailIPDComment"  # Available IPD Comment
    IPDSharing = "IPDSharing"  # Plan to Share IPD
    IPDSharingDescription = "IPDSharingDescription"  # IPD Sharing Description
    IPDSharingInfoType = "IPDSharingInfoType"  # IPD Sharing Info Type
    IPDSharingTimeFrame = "IPDSharingTimeFrame"  # IPD Sharing Time Frame
    IPDSharingAccessCriteria = "IPDSharingAccessCriteria"  # IPD Sharing Access Criteria
    IPDSharingURL = "IPDSharingURL"  # IPD Sharing URL

    # Results: Participant Flow
    FlowPreAssignmentDetails = "FlowPreAssignmentDetails"  # Pre-assignment Details
    FlowRecruitmentDetails = "FlowRecruitmentDetails"  # Recruitment Details
    FlowTypeUnitsAnalyzed = "FlowTypeUnitsAnalyzed"  # Type of Unit Analyzed
    FlowGroupId = "FlowGroupId"  # Arm/Group ID
    FlowGroupTitle = "FlowGroupTitle"  # Arm/Group Title
    FlowGroupDescription = "FlowGroupDescription"  # Arm/Group Description
    FlowPeriodTitle = "FlowPeriodTitle"  # Period Title
    FlowMilestoneType = "FlowMilestoneType"  # Milestone Title
    FlowMilestoneComment = "FlowMilestoneComment"  # Milestone Comment
    FlowAchievementGroupId = "FlowAchievementGroupId"  # Milestone Arm/Group ID
    FlowAchievementComment = "FlowAchievementComment"  # Milestone Arm/Group Comment
    FlowAchievementNumSubjects = "FlowAchievementNumSubjects"  # Number of Milestone Arm/Group Participants
    FlowAchievementNumUnits = "FlowAchievementNumUnits"  # Number of Units
    FlowDropWithdrawType = "FlowDropWithdrawType"  # Reason Not Completed Type
    FlowDropWithdrawComment = "FlowDropWithdrawComment"  # Description of Reason Not Completed
    FlowReasonGroupId = "FlowReasonGroupId"  # Reason Group ID
    FlowReasonComment = "FlowReasonComment"  # Reason Comment
    FlowReasonNumSubjects = "FlowReasonNumSubjects"  # Reason Group Number of Subjects

    # Results: Baseline Characteristics
    BaselinePopulationDescription = "BaselinePopulationDescription"  # Baseline Analysis Population Description
    BaselineTypeUnitsAnalyzed = "BaselineTypeUnitsAnalyzed"  # Type of Units Analyzed
    BaselineGroupId = "BaselineGroupId"  # Arm/Group ID
    BaselineGroupTitle = "BaselineGroupTitle"  # Arm/Group Title
    BaselineGroupDescription = "BaselineGroupDescription"  # Arm/Group Description
    BaselineDenomUnits = "BaselineDenomUnits"  # Overall Number of Units Analyzed
    BaselineDenomCountGroupId = "BaselineDenomCountGroupId"  # Arm/Group ID
    BaselineDenomCountValue = "BaselineDenomCountValue"  # Denom Count Value
    BaselineMeasureTitle = "BaselineMeasureTitle"  # Baseline Measure Title
    BaselineMeasureDescription = "BaselineMeasureDescription"  # Baseline Measure Title for Study-Specified Measure
    BaselineMeasurePopulationDescription = "BaselineMeasurePopulationDescription"  # Baseline Measure Description
    BaselineMeasureParamType = "BaselineMeasureParamType"  # Baseline Measure Type
    BaselineMeasureDispersionType = "BaselineMeasureDispersionType"  # Baseline Measure Dispersion/Precision
    BaselineMeasureUnitOfMeasure = "BaselineMeasureUnitOfMeasure"  # Unit of Measure
    BaselineMeasureCalculatePct = "BaselineMeasureCalculatePct"  # Calculated Percentage
    BaselineMeasureDenomUnitsSelected = "BaselineMeasureDenomUnitsSelected"  # Type of Units Selected
    BaselineMeasureDenomUnits = "BaselineMeasureDenomUnits"  # Analysis Population Type
    BaselineMeasureDenomCountGroupId = "BaselineMeasureDenomCountGroupId"  # Denom Count Group ID
    BaselineMeasureDenomCountValue = "BaselineMeasureDenomCountValue"  # Denom Count Value
    BaselineClassTitle = "BaselineClassTitle"  # Baseline Row Title
    BaselineClassDenomUnits = "BaselineClassDenomUnits"  # Baseline Row Unit of Measure
    BaselineClassDenomCountGroupId = "BaselineClassDenomCountGroupId"  # Class Denom Count Group ID
    BaselineClassDenomCountValue = "BaselineClassDenomCountValue"  # Class Denom Count Value
    BaselineCategoryTitle = "BaselineCategoryTitle"  # Category Title
    BaselineMeasurementGroupId = "BaselineMeasurementGroupId"  # Arm/Group ID
    BaselineMeasurementValue = "BaselineMeasurementValue"  # Measurement Value
    BaselineMeasurementSpread = "BaselineMeasurementSpread"  # Measurement Spread
    BaselineMeasurementLowerLimit = "BaselineMeasurementLowerLimit"  # Measurement Lower Limit
    BaselineMeasurementUpperLimit = "BaselineMeasurementUpperLimit"  # Measurement Upper Limit
    BaselineMeasurementComment = "BaselineMeasurementComment"  # Comments for N/A values

    # Results: Outcome Measures
    OutcomeMeasureType = "OutcomeMeasureType"  # Outcome Measure Type
    OutcomeMeasureTitle = "OutcomeMeasureTitle"  # Outcome Measure Title
    OutcomeMeasureDescription = "OutcomeMeasureDescription"  # Outcome Measure Description
    OutcomeMeasurePopulationDescription = "OutcomeMeasurePopulationDescription"  # Analysis Population Description
    OutcomeMeasureReportingStatus = "OutcomeMeasureReportingStatus"  # Reporting Status
    OutcomeMeasureAnticipatedPostingDate = "OutcomeMeasureAnticipatedPostingDate"  # Anticipated Reporting Date
    OutcomeMeasureParamType = "OutcomeMeasureParamType"  # Outcome Measure Data Type
    OutcomeMeasureDispersionType = "OutcomeMeasureDispersionType"  # Outcome Measure Dispersion/Precision
    OutcomeMeasureUnitOfMeasure = "OutcomeMeasureUnitOfMeasure"  # Unit of Measure
    OutcomeMeasureCalculatePct = "OutcomeMeasureCalculatePct"  # Calculated Percentage
    OutcomeMeasureTimeFrame = "OutcomeMeasureTimeFrame"  # Outcome Measure Time Frame
    OutcomeMeasureTypeUnitsAnalyzed = "OutcomeMeasureTypeUnitsAnalyzed"  # Units Analyzed
    OutcomeMeasureDenomUnitsSelected = "OutcomeMeasureDenomUnitsSelected"  # Denom Units Selected
    OutcomeGroupId = "OutcomeGroupId"  # Outcome Group ID
    OutcomeGroupTitle = "OutcomeGroupTitle"  # Outcome Group Title
    OutcomeGroupDescription = "OutcomeGroupDescription"  # Outcome Group Description
    OutcomeDenomUnits = "OutcomeDenomUnits"  # Outcome Denom Units
    OutcomeDenomCountGroupId = "OutcomeDenomCountGroupId"  # Outcome Denom Count Group ID
    OutcomeDenomCountValue = "OutcomeDenomCountValue"  # Outcome Denom Count Value
    OutcomeClassTitle = "OutcomeClassTitle"  # Outcome Class Title
    OutcomeClassDenomUnits = "OutcomeClassDenomUnits"  # Outcome Class Denom Units
    OutcomeClassDenomCountGroupId = "OutcomeClassDenomCountGroupId"  # Outcome Class Denom Count Group ID
    OutcomeClassDenomCountValue = "OutcomeClassDenomCountValue"  # Outcome Class Denom Count Value
    OutcomeCategoryTitle = "OutcomeCategoryTitle"  # Category Title
    OutcomeMeasurementGroupId = "OutcomeMeasurementGroupId"  # Measurement Group ID
    OutcomeMeasurementValue = "OutcomeMeasurementValue"  # Measurement Value
    OutcomeMeasurementSpread = "OutcomeMeasurementSpread"  # Measurement Spread
    OutcomeMeasurementLowerLimit = "OutcomeMeasurementLowerLimit"  # Measurement Lower Limit
    OutcomeMeasurementUpperLimit = "OutcomeMeasurementUpperLimit"  # Measurement Upper Limit
    OutcomeMeasurementComment = "OutcomeMeasurementComment"  # Comments for N/A values
    OutcomeAnalysisParamType = "OutcomeAnalysisParamType"  # Estimation Parameter
    OutcomeAnalysisParamValue = "OutcomeAnalysisParamValue"  # Estimated Value
    OutcomeAnalysisDispersionType = "OutcomeAnalysisDispersionType"  # Estimation Dispersion Type
    OutcomeAnalysisDispersionValue = "OutcomeAnalysisDispersionValue"  # Parameter Dispersion Value
    OutcomeAnalysisStatisticalMethod = "OutcomeAnalysisStatisticalMethod"  # Statistical Method
    OutcomeAnalysisStatisticalComment = "OutcomeAnalysisStatisticalComment"  # Statistical Comment
    OutcomeAnalysisPValue = "OutcomeAnalysisPValue"  # P-Value
    OutcomeAnalysisPValueComment = "OutcomeAnalysisPValueComment"  # P-Value Comment
    OutcomeAnalysisCINumSides = "OutcomeAnalysisCINumSides"  # Number of Sides for Confidence Interval
    OutcomeAnalysisCIPctValue = "OutcomeAnalysisCIPctValue"  # Percentage for Confidence Interval
    OutcomeAnalysisCILowerLimit = "OutcomeAnalysisCILowerLimit"  # Lower Limit for 2-sided Confidence Interval
    OutcomeAnalysisCIUpperLimit = "OutcomeAnalysisCIUpperLimit"  # Upper Limit for 2-sided Confidence Interval
    OutcomeAnalysisCILowerLimitComment = "OutcomeAnalysisCILowerLimitComment"  # Lower Limit Comment
    OutcomeAnalysisCIUpperLimitComment = "OutcomeAnalysisCIUpperLimitComment"  # Upper Limit Comment
    OutcomeAnalysisEstimateComment = "OutcomeAnalysisEstimateComment"  # Estimation Comment
    OutcomeAnalysisTestedNonInferiority = "OutcomeAnalysisTestedNonInferiority"  # Non-inferiority or Equivalence Test Type
    OutcomeAnalysisNonInferiorityType = "OutcomeAnalysisNonInferiorityType"  # Type of Statistical Test
    OutcomeAnalysisNonInferiorityComment = "OutcomeAnalysisNonInferiorityComment"  # Non-inferiority or Equivalence Comment
    OutcomeAnalysisOtherAnalysisDescription = "OutcomeAnalysisOtherAnalysisDescription"  # Other Statistical Analysis
    OutcomeAnalysisGroupDescription = "OutcomeAnalysisGroupDescription"  # Selected Comparison Group Description
    OutcomeAnalysisGroupId = "OutcomeAnalysisGroupId"  # Outcome Analysis Group IDs

    # Results: Adverse Events
    EventsFrequencyThreshold = "EventsFrequencyThreshold"  # Frequency Threshold
    EventsTimeFrame = "EventsTimeFrame"  # Adverse Event Time Frame
    EventsDescription = "EventsDescription"  # Adverse Event Reporting Description
    EventsAllCauseMortalityComment = "EventsAllCauseMortalityComment"  # All Cause Mortality Comment
    EventGroupId = "EventGroupId"  # Arm/Group ID
    EventGroupTitle = "EventGroupTitle"  # Arm/Group Title
    EventGroupDescription = "EventGroupDescription"  # Arm/Group Description
    EventGroupDeathsNumAffected = "EventGroupDeathsNumAffected"  # Total Number Affected by All-Cause Mortality
    EventGroupDeathsNumAtRisk = "EventGroupDeathsNumAtRisk"  # Total Number at Risk for All-Cause Mortality
    EventGroupSeriousNumAffected = "EventGroupSeriousNumAffected"  # Number Affected by a Serious Adverse Event
    EventGroupSeriousNumAtRisk = "EventGroupSeriousNumAtRisk"  # Number at Risk for a Serious Adverse Event
    EventGroupOtherNumAffected = "EventGroupOtherNumAffected"  # Number Affected by Any Other Adverse Event
    EventGroupOtherNumAtRisk = "EventGroupOtherNumAtRisk"  # Number at Risk for Any Other Adverse Event
    SeriousEventTerm = "SeriousEventTerm"  # Serious Adverse Event Term
    SeriousEventOrganSystem = "SeriousEventOrganSystem"  # Organ System
    SeriousEventSourceVocabulary = "SeriousEventSourceVocabulary"  # Source Vocabulary Name for Serious Adverse Event
    SeriousEventAssessmentType = "SeriousEventAssessmentType"  # Collection Approach
    SeriousEventNotes = "SeriousEventNotes"  # Serious Adverse Event Term Additional Description
    SeriousEventStatsGroupId = "SeriousEventStatsGroupId"  # Group ID
    SeriousEventStatsNumEvents = "SeriousEventStatsNumEvents"  # Number of Serious Events in an Arm/Group
    SeriousEventStatsNumAffected = "SeriousEventStatsNumAffected"  # Number of Participants Affected
    SeriousEventStatsNumAtRisk = "SeriousEventStatsNumAtRisk"  # Number of Participants at Risk
    OtherEventTerm = "OtherEventTerm"  # Other Adverse Event Term
    OtherEventOrganSystem = "OtherEventOrganSystem"  # Other Adverse Event Organ System
    OtherEventSourceVocabulary = "OtherEventSourceVocabulary"  # Other Adverse Event Source Vocabulary
    OtherEventAssessmentType = "OtherEventAssessmentType"  # Other Adverse Event Assessment Type
    OtherEventNotes = "OtherEventNotes"  # Other Adverse Event Notes
    OtherEventStatsGroupId = "OtherEventStatsGroupId"  # Other Event Stats Group ID
    OtherEventStatsNumEvents = "OtherEventStatsNumEvents"  # Other Event Stats Number of Events
    OtherEventStatsNumAffected = "OtherEventStatsNumAffected"  # Other Event Stats Number Affected
    OtherEventStatsNumAtRisk = "OtherEventStatsNumAtRisk"  # Other Event Stats Number at Risk

    # Results: More Info
    LimitationsAndCaveatsDescription = "LimitationsAndCaveatsDescription"  # Limitations and Caveats Description
    AgreementPISponsorEmployee = "AgreementPISponsorEmployee"  # Agreement PI Sponsor Employee
    AgreementRestrictionType = "AgreementRestrictionType"  # Agreement Restriction Type
    AgreementRestrictiveAgreement = "AgreementRestrictiveAgreement"  # Agreement Restrictive Agreement
    AgreementOtherDetails = "AgreementOtherDetails"  # Agreement Other Details
    PointOfContactTitle = "PointOfContactTitle"  # Point of Contact Title
    PointOfContactOrganization = "PointOfContactOrganization"  # Point of Contact Organization
    PointOfContactEMail = "PointOfContactEMail"  # Point of Contact Email
    PointOfContactPhone = "PointOfContactPhone"  # Point of Contact Phone
    PointOfContactPhoneExt = "PointOfContactPhoneExt"  # Point of Contact Phone Extension

    # Annotation / Derived
    UnpostedResponsibleParty = "UnpostedResponsibleParty"  # Responsible Party for Unposted Events
    UnpostedEventType = "UnpostedEventType"  # Study Results Submission Type
    UnpostedEventDate = "UnpostedEventDate"  # Study Results Submission Date
    UnpostedEventDateUnknown = "UnpostedEventDateUnknown"  # Unposted Event Date is Unknown
    ViolationEventType = "ViolationEventType"  # Violation Event Type
    ViolationEventDescription = "ViolationEventDescription"  # Violation Event Type Description
    ViolationEventCreationDate = "ViolationEventCreationDate"  # Violation Event Creation Date
    ViolationEventIssuedDate = "ViolationEventIssuedDate"  # Violation Event Issued Date
    ViolationEventReleaseDate = "ViolationEventReleaseDate"  # Violation Event Released Date
    ViolationEventPostedDate = "ViolationEventPostedDate"  # Violation Event Posted Date

    # Large Documents
    LargeDocNoSAP = "LargeDocNoSAP"  # Document Has No Statistical Analysis Plan (SAP)
    LargeDocTypeAbbrev = "LargeDocTypeAbbrev"  # Document Type
    LargeDocHasProtocol = "LargeDocHasProtocol"  # Document Includes Study Protocol
    LargeDocHasSAP = "LargeDocHasSAP"  # Document Includes Statistical Analysis Plan (SAP)
    LargeDocHasICF = "LargeDocHasICF"  # Document Includes Informed Consent Form (ICF)
    LargeDocLabel = "LargeDocLabel"  # Document Label
    LargeDocDate = "LargeDocDate"  # Document Date
    LargeDocUploadDate = "LargeDocUploadDate"  # Document Uploaded Date
    LargeDocFilename = "LargeDocFilename"  # Document File Name
    LargeDocSize = "LargeDocSize"  # Document File Size

    # Misc / Derived
    VersionHolder = "VersionHolder"  # Version Holder
    RemovedCountry = "RemovedCountry"  # Removed Countries
    EstimatedResultsFirstSubmitDate = "EstimatedResultsFirstSubmitDate"  # Estimated Results First Submitted Date
    FirstMCPPostDate = "FirstMCPPostDate"  # First MCP Posted Date
    FirstMCPPostDateType = "FirstMCPPostDateType"  # First MCP Posted Date Type
    SubmissionReleaseDate = "SubmissionReleaseDate"  # Release Date
    SubmissionUnreleaseDate = "SubmissionUnreleaseDate"  # Unrelease Date
    SubmissionUnreleaseDateUnknown = "SubmissionUnreleaseDateUnknown"  # Unrelease Date Unknown
    SubmissionResetDate = "SubmissionResetDate"  # Reset Date
    SubmissionMCPReleaseN = "SubmissionMCPReleaseN"  # Number of MCPs

    # MeSH / Browse (Derived)
    ConditionMeshId = "ConditionMeshId"  # Condition MeSH ID
    ConditionMeshTerm = "ConditionMeshTerm"  # Condition MeSH Term
    ConditionAncestorId = "ConditionAncestorId"  # Condition Ancestor MeSH ID
    ConditionAncestorTerm = "ConditionAncestorTerm"  # Condition Ancestor MeSH Term
    ConditionBrowseLeafId = "ConditionBrowseLeafId"  # Condition Leaf Topic ID
    ConditionBrowseLeafName = "ConditionBrowseLeafName"  # Condition Leaf Topic Name
    ConditionBrowseLeafAsFound = "ConditionBrowseLeafAsFound"  # Found by Condition Term
    ConditionBrowseLeafRelevance = "ConditionBrowseLeafRelevance"  # Relevance to Condition Leaf Topic
    ConditionBrowseBranchAbbrev = "ConditionBrowseBranchAbbrev"  # Condition Branch Topic Short Name
    ConditionBrowseBranchName = "ConditionBrowseBranchName"  # Condition Branch Topic Name
    InterventionMeshId = "InterventionMeshId"  # Intervention MeSH ID
    InterventionMeshTerm = "InterventionMeshTerm"  # Intervention MeSH Term
    InterventionAncestorId = "InterventionAncestorId"  # Intervention Ancestor MeSH ID
    InterventionAncestorTerm = "InterventionAncestorTerm"  # Intervention Ancestor MeSH Term
    InterventionBrowseLeafId = "InterventionBrowseLeafId"  # Intervention Leaf Topic ID
    InterventionBrowseLeafName = "InterventionBrowseLeafName"  # Intervention Leaf Topic Name
    InterventionBrowseLeafAsFound = "InterventionBrowseLeafAsFound"  # Found by Intervention Term
    InterventionBrowseLeafRelevance = "InterventionBrowseLeafRelevance"  # Relevance to Intervention Leaf Topic
    InterventionBrowseBranchAbbrev = "InterventionBrowseBranchAbbrev"  # Intervention Branch Topic Short Name
    InterventionBrowseBranchName = "InterventionBrowseBranchName"  # Intervention Branch Topic Name

    HasResults = "HasResults"  # Has Results


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
        description="Search by location terms such as facility name or city (e.g., 'Boston', 'Mayo Clinic').",
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
            self.agg_filters,
        ]
        if not any(query_fields):
            raise ValueError(
                "At least one query parameter (query_cond, query_term, query_intr, "
                "query_titles, query_id, query_spons, query_locn, query_patient), "
                "filter_ids, agg_filter_phase, agg_filter_study_type, or agg_filters "
                "must be provided."
            )
        return self


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
        default=None,
        description=(
            "Specific fields to return. If omitted, all fields are returned. "
            "Example: [NCTId, BriefTitle, OverallStatus, Phase]."
        ),
    )


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

