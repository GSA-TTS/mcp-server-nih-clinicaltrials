"""
Import validation tests for the models module refactoring.

These tests ensure that all classes can be imported from the models module
after the refactoring from a single file to a directory structure.
This maintains backward compatibility with existing code.
"""

import pytest


def test_import_enums_from_models():
    """Test that all enum classes can be imported from clinicaltrials.models."""
    from clinicaltrials.models import (
        ResponseFormat,
        MarkupFormat,
        OverallStatus,
        StudyType,
        Phase,
        Sex,
        StandardAge,
        SamplingMethod,
        IpdSharing,
        IpdSharingInfoType,
        OrgStudyIdType,
        SecondaryIdType,
        AgencyClass,
        ExpandedAccessStatus,
        DateType,
        ResponsiblePartyType,
        DesignAllocation,
        InterventionalAssignment,
        PrimaryPurpose,
        ObservationalModel,
        DesignTimePerspective,
        BioSpecRetention,
        EnrollmentType,
        ArmGroupType,
        InterventionType,
        ContactRole,
        OfficialRole,
        RecruitmentStatus,
        ReferenceType,
        MeasureParam,
        MeasureDispersionType,
        OutcomeMeasureType,
        ReportingStatus,
        EventAssessment,
        AgreementRestrictionType,
        BrowseLeafRelevance,
        DesignMasking,
        WhoMasked,
        AnalysisDispersionType,
        ConfidenceIntervalNumSides,
        NonInferiorityType,
        UnpostedEventType,
        ViolationEventType,
    )
    
    # Verify enums have expected values
    assert ResponseFormat.JSON.value == "json"
    assert OverallStatus.RECRUITING.value == "RECRUITING"
    assert Phase.PHASE2.value == "PHASE2"
    assert StudyType.INTERVENTIONAL.value == "INTERVENTIONAL"


def test_import_study_field_from_models():
    """Test that StudyField enum can be imported from clinicaltrials.models."""
    from clinicaltrials.models import StudyField
    
    # Verify it's the StudyField enum with expected members
    assert hasattr(StudyField, "NCTId")
    assert hasattr(StudyField, "BriefTitle")
    assert hasattr(StudyField, "OverallStatus")
    assert StudyField.NCTId.value == "NCTId"


def test_import_search_classes_from_models():
    """Test that search base classes can be imported from clinicaltrials.models."""
    from clinicaltrials.models import StudyQueryParams, StudySearchBase
    
    # Verify they are Pydantic models
    assert hasattr(StudyQueryParams, "model_config")
    assert hasattr(StudySearchBase, "model_config")


def test_import_input_models_from_models():
    """Test that all input models can be imported from clinicaltrials.models."""
    from clinicaltrials.models import (
        GetStudyInput,
        SearchStudiesInput,
        GetFieldValuesInput,
        AnalyzeStudyLocationsInput,
        SearchDatatableInput,
    )
    
    # Verify they are Pydantic models
    assert hasattr(GetStudyInput, "model_config")
    assert hasattr(SearchStudiesInput, "model_config")
    assert hasattr(GetFieldValuesInput, "model_config")
    assert hasattr(AnalyzeStudyLocationsInput, "model_config")
    assert hasattr(SearchDatatableInput, "model_config")


def test_get_study_input_instantiation():
    """Test that GetStudyInput can be instantiated correctly."""
    from clinicaltrials.models import GetStudyInput, ResponseFormat, MarkupFormat
    
    # Test valid instantiation
    input_obj = GetStudyInput(nct_id="NCT00000102")
    assert input_obj.nct_id == "NCT00000102"
    assert input_obj.format == ResponseFormat.JSON
    assert input_obj.markup_format == MarkupFormat.MARKDOWN
    
    # Test with fields (NCT ID must match pattern before normalization)
    from clinicaltrials.models import StudyField
    input_obj = GetStudyInput(
        nct_id="NCT00000103",
        fields=[StudyField.NCTId, StudyField.BriefTitle]
    )
    assert input_obj.nct_id == "NCT00000103"
    assert len(input_obj.fields) == 2


def test_search_studies_input_instantiation():
    """Test that SearchStudiesInput can be instantiated correctly."""
    from clinicaltrials.models import SearchStudiesInput, Phase
    
    # Test valid instantiation with query
    input_obj = SearchStudiesInput(query_cond="diabetes")
    assert input_obj.query_cond == "diabetes"
    assert input_obj.page_size == 20  # default
    
    # Test with phase filter
    input_obj = SearchStudiesInput(
        query_cond="cancer",
        agg_filter_phase=[Phase.PHASE2, Phase.PHASE3]
    )
    assert input_obj.query_cond == "cancer"
    assert Phase.PHASE2 in input_obj.agg_filter_phase


def test_get_field_values_input_instantiation():
    """Test that GetFieldValuesInput can be instantiated correctly."""
    from clinicaltrials.models import GetFieldValuesInput, StudyField
    
    input_obj = GetFieldValuesInput(
        fields=[StudyField.Phase, StudyField.OverallStatus]
    )
    assert len(input_obj.fields) == 2
    assert StudyField.Phase in input_obj.fields


def test_analyze_study_locations_input_instantiation():
    """Test that AnalyzeStudyLocationsInput can be instantiated correctly."""
    from clinicaltrials.models import AnalyzeStudyLocationsInput
    
    input_obj = AnalyzeStudyLocationsInput(
        query_cond="diabetes",
        target_country="Canada"
    )
    assert input_obj.query_cond == "diabetes"
    assert input_obj.target_country == "Canada"


def test_search_datatable_input_instantiation():
    """Test that SearchDatatableInput can be instantiated correctly."""
    from clinicaltrials.models import SearchDatatableInput
    
    input_obj = SearchDatatableInput(
        query_cond="hypertension",
        sort="LastUpdatePostDate:desc"
    )
    assert input_obj.query_cond == "hypertension"
    assert input_obj.sort == "LastUpdatePostDate:desc"


def test_backward_compatibility_existing_imports():
    """Test that existing import patterns in the codebase still work."""
    # Pattern from tools/search_datatable.py
    from clinicaltrials.models import SearchDatatableInput
    assert SearchDatatableInput is not None
    
    # Pattern from tools/analyze_locations.py
    from clinicaltrials.models import AnalyzeStudyLocationsInput
    assert AnalyzeStudyLocationsInput is not None
    
    # Pattern from tools/get_field_values.py
    from clinicaltrials.models import GetFieldValuesInput
    assert GetFieldValuesInput is not None
    
    # Pattern from tools/search_studies.py
    from clinicaltrials.models import ResponseFormat, SearchStudiesInput
    assert ResponseFormat is not None
    assert SearchStudiesInput is not None
    
    # Pattern from tools/get_study.py
    from clinicaltrials.models import GetStudyInput, ResponseFormat as RF
    assert GetStudyInput is not None
    assert RF is not None


def test_all_exports_accessible():
    """Test that all items in __all__ are actually accessible."""
    from clinicaltrials import models
    
    # Get the __all__ list
    all_exports = models.__all__
    
    # Verify each export is accessible
    for export_name in all_exports:
        assert hasattr(models, export_name), f"{export_name} not accessible from models module"
        obj = getattr(models, export_name)
        assert obj is not None, f"{export_name} is None"


def test_no_import_errors():
    """Test that importing the models module doesn't raise any errors."""
    import clinicaltrials.models
    
    # If we got here, no import errors occurred
    assert clinicaltrials.models is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
