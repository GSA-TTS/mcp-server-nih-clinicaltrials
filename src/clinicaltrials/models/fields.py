from enum import Enum

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


# Default fields for search_studies to minimize context window usage
# while providing essential information for initial study screening
DEFAULT_SEARCH_FIELDS = [
    # Identification (4 fields)
    StudyField.NCTId,           # National Clinical Trial ID
    StudyField.BriefTitle,      # Brief Title
    StudyField.OfficialTitle,   # Official Title
    StudyField.Acronym,         # Acronym
    
    # Status (5 fields)
    StudyField.OverallStatus,           # Recruitment status
    StudyField.StartDate,               # Study start date
    StudyField.PrimaryCompletionDate,   # Primary completion date
    StudyField.CompletionDate,          # Full completion date
    StudyField.LastUpdatePostDate,      # Last update timestamp
    
    # Core Study Info (6 fields)
    StudyField.BriefSummary,    # Study summary
    StudyField.Condition,       # Disease/condition
    StudyField.Phase,           # Study phase
    StudyField.StudyType,       # Interventional vs observational
    StudyField.EnrollmentCount, # Number of participants
    StudyField.InterventionName,# Treatment/intervention
    
    # Sponsor (2 fields)
    StudyField.LeadSponsorName,  # Primary sponsor
    StudyField.LeadSponsorClass, # Sponsor type (industry, NIH, etc.)
    
    # Location (2 fields)
    StudyField.LocationCountry,  # Study countries
    StudyField.LocationFacility, # Study sites
]