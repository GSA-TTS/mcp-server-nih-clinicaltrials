"""
Tests for default field behavior in SearchStudiesInput.

These tests verify that:
1. SearchStudiesInput uses DEFAULT_SEARCH_FIELDS by default
2. The default fields list contains the expected 19 essential fields
3. Custom field lists can still be provided
4. The default behavior minimizes context window usage
"""

import pytest


def test_default_search_fields_constant_exists():
    """Test that DEFAULT_SEARCH_FIELDS constant is defined and exported."""
    from clinicaltrials.models.fields import DEFAULT_SEARCH_FIELDS
    
    assert DEFAULT_SEARCH_FIELDS is not None
    assert isinstance(DEFAULT_SEARCH_FIELDS, list)
    assert len(DEFAULT_SEARCH_FIELDS) > 0


def test_default_search_fields_count():
    """Test that DEFAULT_SEARCH_FIELDS contains exactly 19 essential fields."""
    from clinicaltrials.models.fields import DEFAULT_SEARCH_FIELDS
    
    assert len(DEFAULT_SEARCH_FIELDS) == 19, (
        f"Expected 19 default fields for optimal context usage, got {len(DEFAULT_SEARCH_FIELDS)}"
    )


def test_default_search_fields_content():
    """Test that DEFAULT_SEARCH_FIELDS contains the expected essential fields."""
    from clinicaltrials.models.fields import DEFAULT_SEARCH_FIELDS, StudyField
    
    # Identification fields (4)
    assert StudyField.NCTId in DEFAULT_SEARCH_FIELDS
    assert StudyField.BriefTitle in DEFAULT_SEARCH_FIELDS
    assert StudyField.OfficialTitle in DEFAULT_SEARCH_FIELDS
    assert StudyField.Acronym in DEFAULT_SEARCH_FIELDS
    
    # Status fields (5)
    assert StudyField.OverallStatus in DEFAULT_SEARCH_FIELDS
    assert StudyField.StartDate in DEFAULT_SEARCH_FIELDS
    assert StudyField.PrimaryCompletionDate in DEFAULT_SEARCH_FIELDS
    assert StudyField.CompletionDate in DEFAULT_SEARCH_FIELDS
    assert StudyField.LastUpdatePostDate in DEFAULT_SEARCH_FIELDS
    
    # Core study info fields (6)
    assert StudyField.BriefSummary in DEFAULT_SEARCH_FIELDS
    assert StudyField.Condition in DEFAULT_SEARCH_FIELDS
    assert StudyField.Phase in DEFAULT_SEARCH_FIELDS
    assert StudyField.StudyType in DEFAULT_SEARCH_FIELDS
    assert StudyField.EnrollmentCount in DEFAULT_SEARCH_FIELDS
    assert StudyField.InterventionName in DEFAULT_SEARCH_FIELDS
    
    # Sponsor fields (2)
    assert StudyField.LeadSponsorName in DEFAULT_SEARCH_FIELDS
    assert StudyField.LeadSponsorClass in DEFAULT_SEARCH_FIELDS
    
    # Location fields (2)
    assert StudyField.LocationCountry in DEFAULT_SEARCH_FIELDS
    assert StudyField.LocationFacility in DEFAULT_SEARCH_FIELDS


def test_search_studies_input_uses_default_fields():
    """Test that SearchStudiesInput uses DEFAULT_SEARCH_FIELDS by default."""
    from clinicaltrials.models import SearchStudiesInput
    from clinicaltrials.models.fields import DEFAULT_SEARCH_FIELDS
    
    # Create input without specifying fields
    input_obj = SearchStudiesInput(query_cond="diabetes")
    
    # Should have default fields
    assert input_obj.fields is not None
    assert len(input_obj.fields) == len(DEFAULT_SEARCH_FIELDS)
    assert input_obj.fields == DEFAULT_SEARCH_FIELDS


def test_search_studies_input_accepts_custom_fields():
    """Test that SearchStudiesInput can accept custom field lists."""
    from clinicaltrials.models import SearchStudiesInput, StudyField
    
    # Create input with custom fields
    custom_fields = [StudyField.NCTId, StudyField.BriefTitle, StudyField.Phase]
    input_obj = SearchStudiesInput(
        query_cond="cancer",
        fields=custom_fields
    )
    
    # Should use custom fields, not defaults
    assert input_obj.fields == custom_fields
    assert len(input_obj.fields) == 3


def test_search_studies_input_empty_fields_list():
    """Test that an empty fields list can be explicitly provided."""
    from clinicaltrials.models import SearchStudiesInput
    
    # Create input with empty fields list
    input_obj = SearchStudiesInput(
        query_cond="asthma",
        fields=[]
    )
    
    # Should have empty list
    assert input_obj.fields == []
    assert len(input_obj.fields) == 0


def test_default_fields_mutation_safety():
    """Test that modifying fields on one instance doesn't affect defaults."""
    from clinicaltrials.models import SearchStudiesInput
    from clinicaltrials.models.fields import DEFAULT_SEARCH_FIELDS, StudyField
    
    # Create two instances
    input_obj1 = SearchStudiesInput(query_cond="diabetes")
    input_obj2 = SearchStudiesInput(query_cond="cancer")
    
    # Modify fields on first instance
    input_obj1.fields.append(StudyField.DetailedDescription)
    
    # Second instance should not be affected
    assert len(input_obj2.fields) == len(DEFAULT_SEARCH_FIELDS)
    assert StudyField.DetailedDescription not in input_obj2.fields
    
    # Original constant should not be affected
    assert StudyField.DetailedDescription not in DEFAULT_SEARCH_FIELDS


def test_default_fields_are_valid_study_fields():
    """Test that all default fields are valid StudyField enum members."""
    from clinicaltrials.models.fields import DEFAULT_SEARCH_FIELDS, StudyField
    
    for field in DEFAULT_SEARCH_FIELDS:
        assert isinstance(field, StudyField), f"{field} is not a StudyField enum member"
        assert hasattr(StudyField, field.name), f"{field.name} is not a valid StudyField"


def test_default_fields_context_window_optimization():
    """Test that default fields represent significant reduction from all fields."""
    from clinicaltrials.models.fields import DEFAULT_SEARCH_FIELDS, StudyField
    
    # Count total available fields
    total_fields = len([f for f in StudyField])
    default_fields_count = len(DEFAULT_SEARCH_FIELDS)
    
    # Should be less than 10% of total fields (19 out of 394 = ~5%)
    assert default_fields_count < total_fields * 0.1, (
        f"Default fields ({default_fields_count}) should be <10% of total ({total_fields}) "
        f"for meaningful context window reduction"
    )
    
    # More specifically, should achieve ~95% reduction
    reduction_percentage = (1 - default_fields_count / total_fields) * 100
    assert reduction_percentage >= 90, (
        f"Expected ~95% reduction in field count, got {reduction_percentage:.1f}%"
    )


def test_search_studies_input_fields_are_independent_copies():
    """Test that each SearchStudiesInput instance gets an independent copy of default fields."""
    from clinicaltrials.models import SearchStudiesInput
    
    input_obj1 = SearchStudiesInput(query_cond="diabetes")
    input_obj2 = SearchStudiesInput(query_cond="cancer")
    
    # Get the id of the fields lists (memory addresses)
    assert id(input_obj1.fields) != id(input_obj2.fields), (
        "Fields lists should be independent copies, not shared references"
    )


def test_default_fields_includes_critical_identification():
    """Test that default fields include critical identification fields for all use cases."""
    from clinicaltrials.models.fields import DEFAULT_SEARCH_FIELDS, StudyField
    
    # Must include NCTId for identification
    assert StudyField.NCTId in DEFAULT_SEARCH_FIELDS, "NCTId is required for study identification"
    
    # Must include at least one title field
    title_fields = {StudyField.BriefTitle, StudyField.OfficialTitle}
    assert any(f in DEFAULT_SEARCH_FIELDS for f in title_fields), (
        "At least one title field is required"
    )
    
    # Must include status for filtering
    assert StudyField.OverallStatus in DEFAULT_SEARCH_FIELDS, (
        "OverallStatus is required for recruitment filtering"
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
