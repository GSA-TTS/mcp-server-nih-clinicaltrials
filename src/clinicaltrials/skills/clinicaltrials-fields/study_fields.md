# StudyField Names

Complete list of valid field names for the `fields` parameter on
`clinicaltrials_search_studies`, `clinicaltrials_get_study`, and
`clinicaltrials_get_field_values`. Names are case-sensitive and must match
exactly. Sourced from the ClinicalTrials.gov `GET /studies/metadata` endpoint.

## Identification

- `NCTId` — National Clinical Trial (NCT) Identification Number
- `NCTIdAlias` — Obsolete or duplicate NCT associated with a published NCT
- `OrgStudyId` — Organization's Unique Protocol Identification Number
- `OrgStudyIdType` — Organization ID Type
- `OrgStudyIdLink` — Organization ID Link
- `SecondaryId` — Secondary ID
- `SecondaryIdType` — Secondary ID Type
- `SecondaryIdDomain` — Secondary ID Description based on ID Type selected
- `SecondaryIdLink` — Secondary ID Link
- `BriefTitle` — Brief Title
- `OfficialTitle` — Official Title
- `Acronym` — Acronym
- `OrgFullName` — Organization Full Name
- `OrgClass` — Organization type

## Status

- `StatusVerifiedDate` — Record Verification Date
- `OverallStatus` — Overall Recruitment Status or Expanded Access Status
- `LastKnownStatus` — Last Known Status
- `DelayedPosting` — Delayed Posting
- `WhyStopped` — Reason why a study stopped
- `HasExpandedAccess` — Has EA for compassionate use
- `ExpandedAccessNCTId` — NCT of an EA study
- `ExpandedAccessStatusForNCTId` — EA Recruitment Status
- `StartDate` — Study Start Date
- `StartDateType` — Study Start Date Type
- `PrimaryCompletionDate` — Primary Completion Date
- `PrimaryCompletionDateType` — Primary Completion Date Type
- `CompletionDate` — Study Completion Date
- `CompletionDateType` — Study Completion Date Type
- `StudyFirstSubmitDate` — Study First Submitted Date
- `StudyFirstSubmitQCDate` — Study First Submission Date that Met QC Criteria
- `StudyFirstPostDate` — Study First Posted Date
- `StudyFirstPostDateType` — First Study Posted Date Type
- `ResultsWaived` — Results Waived
- `ResultsFirstSubmitDate` — Results First Submitted Date
- `ResultsFirstSubmitQCDate` — Results First Submitted that Met QC Criteria
- `ResultsFirstPostDate` — Results First Posted Date
- `ResultsFirstPostDateType` — Results First Posted Date Type
- `DispFirstSubmitDate` — Certification/Extension First Submitted Date
- `DispFirstSubmitQCDate` — Certification/Extension First Submitted that Passed QC Review
- `DispFirstPostDate` — Certification/Extension First Posted Date
- `DispFirstPostDateType` — Certification/Extension First Posted Date Type
- `LastUpdateSubmitDate` — Last Update Submitted Date
- `LastUpdatePostDate` — Last Update Posted Date
- `LastUpdatePostDateType` — Last Update Posted Date Type

## Sponsor / Responsible Party

- `ResponsiblePartyType` — Responsible Party Type
- `ResponsiblePartyInvestigatorFullName` — Responsible Party Investigator Full Name
- `ResponsiblePartyInvestigatorTitle` — Responsible Party Investigator Title
- `ResponsiblePartyInvestigatorAffiliation` — Responsible Party Investigator Affiliation
- `ResponsiblePartyOldNameTitle` — Older format for Responsible Party Investigator Title
- `ResponsiblePartyOldOrganization` — Older format for Responsible Party Investigator Organization
- `LeadSponsorName` — Lead Sponsor Name
- `LeadSponsorClass` — Lead Sponsor Type
- `CollaboratorName` — Collaborator Name
- `CollaboratorClass` — Collaborator Type

## Oversight

- `OversightHasDMC` — Has Data Monitoring Committee (DMC)
- `IsFDARegulatedDrug` — Is FDA Regulated Drug
- `IsFDARegulatedDevice` — Is FDA Regulated Device
- `IsUnapprovedDevice` — Is Unapproved Device
- `IsPPSD` — Pediatric Postmarket Surveillance of a Device Product
- `IsUSExport` — Product Exported from US
- `FDAAA801Violation` — FDA AA 801 Violation

## Description

- `BriefSummary` — Brief Summary
- `DetailedDescription` — Detailed Description

## Conditions / Keywords

- `Condition` — Condition/Disease
- `Keyword` — Keyword

## Design

- `StudyType` — Study Type
- `NPtrsToThisExpAccNCTId` — Number of References to an Expanded Access Study
- `ExpAccTypeIndividual` — Individual Patients
- `ExpAccTypeIntermediate` — Intermediate-type Population
- `ExpAccTypeTreatment` — Treatment IND/Protocol
- `PatientRegistry` — Patient Registry
- `TargetDuration` — Target Follow-Up Duration
- `Phase` — Study Phase
- `DesignAllocation` — Design Allocation
- `DesignInterventionModel` — Interventional Study Design
- `DesignInterventionModelDescription` — Interventional Study Design Description
- `DesignPrimaryPurpose` — Design Primary Purpose
- `DesignObservationalModel` — Observational Study Model
- `DesignTimePerspective` — Time Perspective
- `DesignMasking` — Design Masking
- `DesignMaskingDescription` — Masking Description
- `DesignWhoMasked` — Who is Masked
- `BioSpecRetention` — Biospecimen Retention
- `BioSpecDescription` — Biospecimen Description
- `EnrollmentCount` — Enrollment
- `EnrollmentType` — Enrollment Type

## Arms / Interventions

- `ArmGroupLabel` — Arm Group Label
- `ArmGroupType` — Arm Group Type
- `ArmGroupDescription` — Arm Description for INT, Group/Cohort Description for OBS
- `ArmGroupInterventionName` — Arm/Group that Receives a Specific Intervention
- `InterventionType` — Intervention/Treatment Type
- `InterventionName` — Intervention Name
- `InterventionDescription` — Intervention Description
- `InterventionArmGroupLabel` — Arm Group Label for Intervention
- `InterventionOtherName` — Other Intervention Name

## Outcomes

- `PrimaryOutcomeMeasure` — Primary Outcome Title
- `PrimaryOutcomeDescription` — Primary Outcome Measure Description
- `PrimaryOutcomeTimeFrame` — Primary Outcome Measure Time Frame
- `SecondaryOutcomeMeasure` — Secondary Outcome Measure Title
- `SecondaryOutcomeDescription` — Secondary Outcome Measure Description
- `SecondaryOutcomeTimeFrame` — Secondary Outcome Measure Time Frame
- `OtherOutcomeMeasure` — Other Outcome Measure Title
- `OtherOutcomeDescription` — Other Outcome Measure Description
- `OtherOutcomeTimeFrame` — Other Outcome Measure Time Frame

## Eligibility

- `EligibilityCriteria` — Inclusion and exclusion eligibility criteria
- `HealthyVolunteers` — Accepts Healthy Volunteers
- `Sex` — Sex/Gender
- `GenderBased` — Gender-Based Eligibility
- `GenderDescription` — Gender Description
- `MinimumAge` — Minimum Age
- `MaximumAge` — Maximum Age
- `StdAge` — Age Group
- `StudyPopulation` — Study Population Description
- `SamplingMethod` — Sampling Method

## Contacts / Locations

- `CentralContactName` — Central Contact Name
- `CentralContactRole` — Central Contact Role
- `CentralContactPhone` — Central Contact Phone
- `CentralContactPhoneExt` — Central Contact Phone Ext
- `CentralContactEMail` — Central Contact EMail
- `OverallOfficialName` — Overall Official Name
- `OverallOfficialAffiliation` — Overall Official Affiliation
- `OverallOfficialRole` — Overall Official Role
- `LocationFacility` — Facility Name
- `LocationStatus` — Individual site recruitment status
- `LocationCity` — City
- `LocationState` — State
- `LocationZip` — Zipcode
- `LocationCountry` — Country
- `LocationContactName` — Location Contact Name
- `LocationContactRole` — Location Contact Role
- `LocationContactPhone` — Location Contact Phone
- `LocationContactPhoneExt` — Location Contact Phone Ext
- `LocationContactEMail` — Location Contact EMail
- `LocationGeoPoint` — Location Geo Point

## References / Links

- `ReferencePMID` — PubMed Identifier
- `ReferenceType` — Reference Type
- `ReferenceCitation` — Reference Citation
- `RetractionPMID` — PMID for Publication Retraction
- `RetractionSource` — Retraction Source
- `SeeAlsoLinkLabel` — See Also Link Label Title
- `SeeAlsoLinkURL` — See Also Link URL

## IPD Sharing

- `AvailIPDId` — Available IPD ID
- `AvailIPDType` — Available IPD Type
- `AvailIPDURL` — Available IPD URL
- `AvailIPDComment` — Available IPD Comment
- `IPDSharing` — Plan to Share IPD
- `IPDSharingDescription` — IPD Sharing Description
- `IPDSharingInfoType` — IPD Sharing Info Type
- `IPDSharingTimeFrame` — IPD Sharing Time Frame
- `IPDSharingAccessCriteria` — IPD Sharing Access Criteria
- `IPDSharingURL` — IPD Sharing URL

## Results: Participant Flow

- `FlowPreAssignmentDetails` — Pre-assignment Details
- `FlowRecruitmentDetails` — Recruitment Details
- `FlowTypeUnitsAnalyzed` — Type of Unit Analyzed
- `FlowGroupId` — Arm/Group ID
- `FlowGroupTitle` — Arm/Group Title
- `FlowGroupDescription` — Arm/Group Description
- `FlowPeriodTitle` — Period Title
- `FlowMilestoneType` — Milestone Title
- `FlowMilestoneComment` — Milestone Comment
- `FlowAchievementGroupId` — Milestone Arm/Group ID
- `FlowAchievementComment` — Milestone Arm/Group Comment
- `FlowAchievementNumSubjects` — Number of Milestone Arm/Group Participants
- `FlowAchievementNumUnits` — Number of Units
- `FlowDropWithdrawType` — Reason Not Completed Type
- `FlowDropWithdrawComment` — Description of Reason Not Completed
- `FlowReasonGroupId` — Reason Group ID
- `FlowReasonComment` — Reason Comment
- `FlowReasonNumSubjects` — Reason Group Number of Subjects

## Results: Baseline Characteristics

- `BaselinePopulationDescription` — Baseline Analysis Population Description
- `BaselineTypeUnitsAnalyzed` — Type of Units Analyzed
- `BaselineGroupId` — Arm/Group ID
- `BaselineGroupTitle` — Arm/Group Title
- `BaselineGroupDescription` — Arm/Group Description
- `BaselineDenomUnits` — Overall Number of Units Analyzed
- `BaselineDenomCountGroupId` — Arm/Group ID
- `BaselineDenomCountValue` — Denom Count Value
- `BaselineMeasureTitle` — Baseline Measure Title
- `BaselineMeasureDescription` — Baseline Measure Title for Study-Specified Measure
- `BaselineMeasurePopulationDescription` — Baseline Measure Description
- `BaselineMeasureParamType` — Baseline Measure Type
- `BaselineMeasureDispersionType` — Baseline Measure Dispersion/Precision
- `BaselineMeasureUnitOfMeasure` — Unit of Measure
- `BaselineMeasureCalculatePct` — Calculated Percentage
- `BaselineMeasureDenomUnitsSelected` — Type of Units Selected
- `BaselineMeasureDenomUnits` — Analysis Population Type
- `BaselineMeasureDenomCountGroupId` — Denom Count Group ID
- `BaselineMeasureDenomCountValue` — Denom Count Value
- `BaselineClassTitle` — Baseline Row Title
- `BaselineClassDenomUnits` — Baseline Row Unit of Measure
- `BaselineClassDenomCountGroupId` — Class Denom Count Group ID
- `BaselineClassDenomCountValue` — Class Denom Count Value
- `BaselineCategoryTitle` — Category Title
- `BaselineMeasurementGroupId` — Arm/Group ID
- `BaselineMeasurementValue` — Measurement Value
- `BaselineMeasurementSpread` — Measurement Spread
- `BaselineMeasurementLowerLimit` — Measurement Lower Limit
- `BaselineMeasurementUpperLimit` — Measurement Upper Limit
- `BaselineMeasurementComment` — Comments for N/A values

## Results: Outcome Measures

- `OutcomeMeasureType` — Outcome Measure Type
- `OutcomeMeasureTitle` — Outcome Measure Title
- `OutcomeMeasureDescription` — Outcome Measure Description
- `OutcomeMeasurePopulationDescription` — Analysis Population Description
- `OutcomeMeasureReportingStatus` — Reporting Status
- `OutcomeMeasureAnticipatedPostingDate` — Anticipated Reporting Date
- `OutcomeMeasureParamType` — Outcome Measure Data Type
- `OutcomeMeasureDispersionType` — Outcome Measure Dispersion/Precision
- `OutcomeMeasureUnitOfMeasure` — Unit of Measure
- `OutcomeMeasureCalculatePct` — Calculated Percentage
- `OutcomeMeasureTimeFrame` — Outcome Measure Time Frame
- `OutcomeMeasureTypeUnitsAnalyzed` — Units Analyzed
- `OutcomeMeasureDenomUnitsSelected` — Denom Units Selected
- `OutcomeGroupId` — Outcome Group ID
- `OutcomeGroupTitle` — Outcome Group Title
- `OutcomeGroupDescription` — Outcome Group Description
- `OutcomeDenomUnits` — Outcome Denom Units
- `OutcomeDenomCountGroupId` — Outcome Denom Count Group ID
- `OutcomeDenomCountValue` — Outcome Denom Count Value
- `OutcomeClassTitle` — Outcome Class Title
- `OutcomeClassDenomUnits` — Outcome Class Denom Units
- `OutcomeClassDenomCountGroupId` — Outcome Class Denom Count Group ID
- `OutcomeClassDenomCountValue` — Outcome Class Denom Count Value
- `OutcomeCategoryTitle` — Category Title
- `OutcomeMeasurementGroupId` — Measurement Group ID
- `OutcomeMeasurementValue` — Measurement Value
- `OutcomeMeasurementSpread` — Measurement Spread
- `OutcomeMeasurementLowerLimit` — Measurement Lower Limit
- `OutcomeMeasurementUpperLimit` — Measurement Upper Limit
- `OutcomeMeasurementComment` — Comments for N/A values
- `OutcomeAnalysisParamType` — Estimation Parameter
- `OutcomeAnalysisParamValue` — Estimated Value
- `OutcomeAnalysisDispersionType` — Estimation Dispersion Type
- `OutcomeAnalysisDispersionValue` — Parameter Dispersion Value
- `OutcomeAnalysisStatisticalMethod` — Statistical Method
- `OutcomeAnalysisStatisticalComment` — Statistical Comment
- `OutcomeAnalysisPValue` — P-Value
- `OutcomeAnalysisPValueComment` — P-Value Comment
- `OutcomeAnalysisCINumSides` — Number of Sides for Confidence Interval
- `OutcomeAnalysisCIPctValue` — Percentage for Confidence Interval
- `OutcomeAnalysisCILowerLimit` — Lower Limit for 2-sided Confidence Interval
- `OutcomeAnalysisCIUpperLimit` — Upper Limit for 2-sided Confidence Interval
- `OutcomeAnalysisCILowerLimitComment` — Lower Limit Comment
- `OutcomeAnalysisCIUpperLimitComment` — Upper Limit Comment
- `OutcomeAnalysisEstimateComment` — Estimation Comment
- `OutcomeAnalysisTestedNonInferiority` — Non-inferiority or Equivalence Test Type
- `OutcomeAnalysisNonInferiorityType` — Type of Statistical Test
- `OutcomeAnalysisNonInferiorityComment` — Non-inferiority or Equivalence Comment
- `OutcomeAnalysisOtherAnalysisDescription` — Other Statistical Analysis
- `OutcomeAnalysisGroupDescription` — Selected Comparison Group Description
- `OutcomeAnalysisGroupId` — Outcome Analysis Group IDs

## Results: Adverse Events

- `EventsFrequencyThreshold` — Frequency Threshold
- `EventsTimeFrame` — Adverse Event Time Frame
- `EventsDescription` — Adverse Event Reporting Description
- `EventsAllCauseMortalityComment` — All Cause Mortality Comment
- `EventGroupId` — Arm/Group ID
- `EventGroupTitle` — Arm/Group Title
- `EventGroupDescription` — Arm/Group Description
- `EventGroupDeathsNumAffected` — Total Number Affected by All-Cause Mortality
- `EventGroupDeathsNumAtRisk` — Total Number at Risk for All-Cause Mortality
- `EventGroupSeriousNumAffected` — Number Affected by a Serious Adverse Event
- `EventGroupSeriousNumAtRisk` — Number at Risk for a Serious Adverse Event
- `EventGroupOtherNumAffected` — Number Affected by Any Other Adverse Event
- `EventGroupOtherNumAtRisk` — Number at Risk for Any Other Adverse Event
- `SeriousEventTerm` — Serious Adverse Event Term
- `SeriousEventOrganSystem` — Organ System
- `SeriousEventSourceVocabulary` — Source Vocabulary Name for Serious Adverse Event
- `SeriousEventAssessmentType` — Collection Approach
- `SeriousEventNotes` — Serious Adverse Event Term Additional Description
- `SeriousEventStatsGroupId` — Group ID
- `SeriousEventStatsNumEvents` — Number of Serious Events in an Arm/Group
- `SeriousEventStatsNumAffected` — Number of Participants Affected
- `SeriousEventStatsNumAtRisk` — Number of Participants at Risk
- `OtherEventTerm` — Other Adverse Event Term
- `OtherEventOrganSystem` — Other Adverse Event Organ System
- `OtherEventSourceVocabulary` — Other Adverse Event Source Vocabulary
- `OtherEventAssessmentType` — Other Adverse Event Assessment Type
- `OtherEventNotes` — Other Adverse Event Notes
- `OtherEventStatsGroupId` — Other Event Stats Group ID
- `OtherEventStatsNumEvents` — Other Event Stats Number of Events
- `OtherEventStatsNumAffected` — Other Event Stats Number Affected
- `OtherEventStatsNumAtRisk` — Other Event Stats Number at Risk

## Results: More Info

- `LimitationsAndCaveatsDescription` — Limitations and Caveats Description
- `AgreementPISponsorEmployee` — Agreement PI Sponsor Employee
- `AgreementRestrictionType` — Agreement Restriction Type
- `AgreementRestrictiveAgreement` — Agreement Restrictive Agreement
- `AgreementOtherDetails` — Agreement Other Details
- `PointOfContactTitle` — Point of Contact Title
- `PointOfContactOrganization` — Point of Contact Organization
- `PointOfContactEMail` — Point of Contact Email
- `PointOfContactPhone` — Point of Contact Phone
- `PointOfContactPhoneExt` — Point of Contact Phone Extension

## Annotation / Derived

- `UnpostedResponsibleParty` — Responsible Party for Unposted Events
- `UnpostedEventType` — Study Results Submission Type
- `UnpostedEventDate` — Study Results Submission Date
- `UnpostedEventDateUnknown` — Unposted Event Date is Unknown
- `ViolationEventType` — Violation Event Type
- `ViolationEventDescription` — Violation Event Type Description
- `ViolationEventCreationDate` — Violation Event Creation Date
- `ViolationEventIssuedDate` — Violation Event Issued Date
- `ViolationEventReleaseDate` — Violation Event Released Date
- `ViolationEventPostedDate` — Violation Event Posted Date

## Large Documents

- `LargeDocNoSAP` — Document Has No Statistical Analysis Plan (SAP)
- `LargeDocTypeAbbrev` — Document Type
- `LargeDocHasProtocol` — Document Includes Study Protocol
- `LargeDocHasSAP` — Document Includes Statistical Analysis Plan (SAP)
- `LargeDocHasICF` — Document Includes Informed Consent Form (ICF)
- `LargeDocLabel` — Document Label
- `LargeDocDate` — Document Date
- `LargeDocUploadDate` — Document Uploaded Date
- `LargeDocFilename` — Document File Name
- `LargeDocSize` — Document File Size

## Misc / Derived

- `VersionHolder` — Version Holder
- `RemovedCountry` — Removed Countries
- `EstimatedResultsFirstSubmitDate` — Estimated Results First Submitted Date
- `FirstMCPPostDate` — First MCP Posted Date
- `FirstMCPPostDateType` — First MCP Posted Date Type
- `SubmissionReleaseDate` — Release Date
- `SubmissionUnreleaseDate` — Unrelease Date
- `SubmissionUnreleaseDateUnknown` — Unrelease Date Unknown
- `SubmissionResetDate` — Reset Date
- `SubmissionMCPReleaseN` — Number of MCPs

## MeSH / Browse (Derived)

- `ConditionMeshId` — Condition MeSH ID
- `ConditionMeshTerm` — Condition MeSH Term
- `ConditionAncestorId` — Condition Ancestor MeSH ID
- `ConditionAncestorTerm` — Condition Ancestor MeSH Term
- `ConditionBrowseLeafId` — Condition Leaf Topic ID
- `ConditionBrowseLeafName` — Condition Leaf Topic Name
- `ConditionBrowseLeafAsFound` — Found by Condition Term
- `ConditionBrowseLeafRelevance` — Relevance to Condition Leaf Topic
- `ConditionBrowseBranchAbbrev` — Condition Branch Topic Short Name
- `ConditionBrowseBranchName` — Condition Branch Topic Name
- `InterventionMeshId` — Intervention MeSH ID
- `InterventionMeshTerm` — Intervention MeSH Term
- `InterventionAncestorId` — Intervention Ancestor MeSH ID
- `InterventionAncestorTerm` — Intervention Ancestor MeSH Term
- `InterventionBrowseLeafId` — Intervention Leaf Topic ID
- `InterventionBrowseLeafName` — Intervention Leaf Topic Name
- `InterventionBrowseLeafAsFound` — Found by Intervention Term
- `InterventionBrowseLeafRelevance` — Relevance to Intervention Leaf Topic
- `InterventionBrowseBranchAbbrev` — Intervention Branch Topic Short Name
- `InterventionBrowseBranchName` — Intervention Branch Topic Name
- `HasResults` — Has Results
