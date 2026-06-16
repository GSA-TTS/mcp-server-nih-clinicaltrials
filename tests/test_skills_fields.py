"""Tests for the field/value skill migration and string-based fields params.

Covers:
- StudyField string validation helper (accepts strings and enum members).
- The three models whose `fields` parameter is now list[str].
- Presence and loadability of the bundled skill files (CWD-independent).
"""

import json
from pathlib import Path

import pytest

from clinicaltrials.models import (
    GetStudyInput,
    SearchStudiesInput,
    GetFieldValuesInput,
    StudyField,
)
from clinicaltrials.models.fields import (
    DEFAULT_SEARCH_FIELDS,
    DEFAULT_SEARCH_FIELDS_STR,
    STUDY_FIELDS_SKILL_RESOURCE,
    validate_study_fields,
)

SKILL_DIR = (
    Path(__file__).resolve().parents[1]
    / "src"
    / "clinicaltrials"
    / "skills"
    / "clinicaltrials-fields"
)


# --- validate_study_fields ------------------------------------------------


def test_validate_accepts_strings():
    assert validate_study_fields(["NCTId", "BriefTitle"]) == ["NCTId", "BriefTitle"]


def test_validate_accepts_enum_members():
    result = validate_study_fields([StudyField.NCTId, StudyField.Phase])
    assert result == ["NCTId", "Phase"]
    assert all(isinstance(x, str) for x in result)


def test_validate_accepts_mixed():
    result = validate_study_fields([StudyField.NCTId, "BriefTitle"])
    assert result == ["NCTId", "BriefTitle"]


def test_validate_rejects_invalid_with_skill_pointer():
    with pytest.raises(ValueError) as exc:
        validate_study_fields(["NCTId", "NotAField"])
    msg = str(exc.value)
    assert "NotAField" in msg
    assert STUDY_FIELDS_SKILL_RESOURCE in msg


# --- model integration ----------------------------------------------------


def test_search_studies_default_fields_populated():
    obj = SearchStudiesInput(query_cond="diabetes")
    assert obj.fields == DEFAULT_SEARCH_FIELDS_STR
    assert all(isinstance(f, str) for f in obj.fields)


def test_search_studies_accepts_enum_members_backcompat():
    obj = SearchStudiesInput(
        query_cond="cancer",
        fields=[StudyField.NCTId, StudyField.BriefTitle],
    )
    assert obj.fields == ["NCTId", "BriefTitle"]


def test_search_studies_rejects_invalid_field():
    with pytest.raises(ValueError):
        SearchStudiesInput(query_cond="cancer", fields=["Bogus"])


def test_get_study_fields_optional_and_validated():
    assert GetStudyInput(nct_id="NCT00000102").fields is None
    obj = GetStudyInput(nct_id="NCT00000102", fields=["NCTId", "Phase"])
    assert obj.fields == ["NCTId", "Phase"]


def test_get_field_values_requires_valid_fields():
    obj = GetFieldValuesInput(fields=["Phase"])
    assert obj.fields == ["Phase"]
    with pytest.raises(ValueError):
        GetFieldValuesInput(fields=["NopeField"])


def test_default_str_list_matches_enum_default():
    assert DEFAULT_SEARCH_FIELDS_STR == [f.value for f in DEFAULT_SEARCH_FIELDS]


# --- skill files ----------------------------------------------------------


def test_skill_files_exist():
    assert (SKILL_DIR / "SKILL.md").is_file()
    assert (SKILL_DIR / "study_fields.md").is_file()
    assert (SKILL_DIR / "enum_values.md").is_file()


def test_study_fields_doc_lists_all_enum_members():
    text = (SKILL_DIR / "study_fields.md").read_text(encoding="utf-8")
    for member in StudyField:
        assert f"`{member.value}`" in text, f"{member.value} missing from skill doc"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
