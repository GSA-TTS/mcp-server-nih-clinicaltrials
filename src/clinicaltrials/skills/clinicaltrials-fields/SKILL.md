---
description: Allowable field names and enumerated values for ClinicalTrials.gov query/filter parameters.
---

# ClinicalTrials.gov Field & Value Reference

This skill documents the allowable values for parameters used by the
ClinicalTrials.gov MCP server tools. Read it when you need to know which
field names or enumerated values are valid for a tool's parameters.

## When to use this skill

- A tool's `fields` parameter (e.g. on `clinicaltrials_search_studies`,
  `clinicaltrials_get_study`, `clinicaltrials_get_field_values`) accepts
  study field **names**. The full catalog of valid names is large and is
  kept out of the tool schemas to save space. Look it up here when you
  need a field that is not in the default set.
- Filter parameters (e.g. `filter_overall_status`, `agg_filter_phase`)
  accept enumerated values. The exact accepted values are listed here.

## Supporting files

This skill keeps the large catalogs in separate files so this main file
stays small. Read the relevant supporting file only when you need it:

- **`study_fields.md`** — The complete list of valid `StudyField` names
  (used by every `fields` parameter), grouped by category, each with a
  short description.
- **`enum_values.md`** — The accepted values for enumerated parameters
  (recruitment status, phase, study type, masking, etc.).

## Quick notes

- Field names are case-sensitive and must match exactly (e.g. `NCTId`,
  `BriefTitle`, `OverallStatus`).
- The `fields` parameter on `clinicaltrials_search_studies` defaults to a
  curated set of essential fields. Override it only when you need
  something specific; for the complete record of a single study, use
  `clinicaltrials_get_study`.
- Enumerated filter values must be passed exactly as listed in
  `enum_values.md` (e.g. `RECRUITING`, `PHASE2`, `INTERVENTIONAL`).
