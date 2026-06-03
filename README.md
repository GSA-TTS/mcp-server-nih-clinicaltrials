# ClinicalTrials.gov MCP Server

An MCP (Model Context Protocol) server that exposes the [ClinicalTrials.gov v2 API](https://clinicaltrials.gov/data-api/api) as tools for LLM agents. Supports searching, retrieving, and analyzing clinical study data from the full registry of 570,000+ studies.

## Tools

### `clinicaltrials_get_study`
Retrieve a single study record by NCT ID.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `nct_id` | string | Yes | NCT identifier, e.g. `NCT00000102` |
| `fields` | `StudyField[]` | No | Specific fields to return; omit for all fields |
| `format` | `json` \| `csv` | No | Response format (default: `json`) |
| `markup_format` | `markdown` \| `legacy` | No | Text markup format (default: `markdown`) |

### `clinicaltrials_search_studies`
Search studies by condition, intervention, sponsor, location, and more. Returns paginated results.

**Query parameters** (at least one required):

| Parameter | Description |
|---|---|
| `query_cond` | Condition or disease (e.g. `diabetes`) |
| `query_term` | General keyword search; also matches enum-typed fields (Phase, StudyType, InterventionType, etc.) when exact enum values are provided |
| `query_intr` | Intervention or treatment name; also matches `InterventionType` and `ArmGroupType` enum values |
| `query_titles` | Search within study titles only |
| `query_id` | NCT ID or other study identifier |
| `query_spons` | Sponsor or collaborator name |
| `query_locn` | Location search (text or AREA syntax: `AREA[LocationState]MA`, `AREA[LocationCountry]US`) |
| `query_patient` | Plain-language patient-friendly search; also matches `StandardAge`, `InterventionalAssignment`, `DesignMasking`, `WhoMasked`, `ObservationalModel`, `PrimaryPurpose`, and `DesignTimePerspective` enum values |

**Filters:**

| Parameter | Type | Description |
|---|---|---|
| `filter_overall_status` | `OverallStatus[]` | Recruitment status (e.g. `[RECRUITING, NOT_YET_RECRUITING]`) |
| `filter_geo` | string | Geographic radius, e.g. `distance(39.0,-77.0,50mi)` |
| `filter_ids` | `string[]` | List of specific NCT IDs |
| `post_filter_overall_status` | `OverallStatus[]` | Status filter applied after aggregation counts |
| `post_filter_geo` | string | Geo filter applied after aggregation counts |
| `agg_filter_phase` | `Phase[]` | Filter by phase (e.g. `[PHASE2, PHASE3]`) |
| `agg_filter_study_type` | `StudyType[]` | Filter by study type (e.g. `[INTERVENTIONAL]`) |
| `agg_filters` | string | Raw aggregation filter string for advanced use; cannot be combined with `agg_filter_phase` or `agg_filter_study_type` |

**Pagination & output:**

| Parameter | Default | Description |
|---|---|---|
| `sort` | — | Sort field and direction, e.g. `LastUpdatePostDate:desc` |
| `page_size` | `20` | Results per page (1–1000) |
| `page_token` | — | Cursor from previous response's `nextPageToken` |
| `count_total` | `false` | Include total match count in response |
| `fields` | all | Specific `StudyField` values to return |
| `format` | `json` | `json` or `csv` |
| `markup_format` | `markdown` | `markdown` or `legacy` |

### `clinicaltrials_search_datatable`
Same search interface as `clinicaltrials_search_studies` but renders all matching results as an interactive, sortable, paginated table. Fetches all pages automatically. Each row shows NCT ID, title, status, phase, conditions, interventions, sponsor, start date, and enrollment count.

Accepts the same query, filter, and sort parameters as `clinicaltrials_search_studies` (excluding pagination and output format options).

### `clinicaltrials_get_field_values`
Get the distribution of values across all studies for one or more fields. Useful for understanding what values exist and how common they are (e.g. study counts per phase, per country, per status).

| Parameter | Type | Required | Description |
|---|---|---|---|
| `fields` | `StudyField[]` | Yes | Fields to get distributions for |

Works best with enumerable fields: `Phase`, `OverallStatus`, `StudyType`, `Sex`, `StdAge`, `LeadSponsorClass`, `InterventionType`, `LocationCountry`, `DesignAllocation`, `IsFDARegulatedDrug`, `HasResults`, `IPDSharing`.

### `clinicaltrials_analyze_study_locations`
Analyze the geographic distribution of locations across a set of studies. Pages through all matching results and classifies each study relative to a target country:

- `only_in_target` — all locations are in the target country
- `mixed` — locations in both the target country and at least one other
- `not_in_target` — no locations in the target country
- `no_location_data` — no location country data present

Also returns a frequency table of every country seen, sorted by count descending.

Accepts the same query and filter parameters as `clinicaltrials_search_studies`, plus:

| Parameter | Default | Description |
|---|---|---|
| `target_country` | `United States` | Reference country for classification (case-insensitive) |

## Field Selection

All tools that return study records accept a `fields` parameter typed as `List[StudyField]`. The `StudyField` enum contains all 342 valid field names sourced from the ClinicalTrials.gov metadata API, grouped by section:

- **Identification**: `NCTId`, `BriefTitle`, `OfficialTitle`, `Acronym`, `OrgFullName`, ...
- **Status**: `OverallStatus`, `StartDate`, `CompletionDate`, `LastUpdatePostDate`, ...
- **Sponsor**: `LeadSponsorName`, `LeadSponsorClass`, `CollaboratorName`, ...
- **Design**: `Phase`, `StudyType`, `DesignAllocation`, `DesignMasking`, `EnrollmentCount`, ...
- **Arms / Interventions**: `InterventionType`, `InterventionName`, `ArmGroupLabel`, ...
- **Outcomes**: `PrimaryOutcomeMeasure`, `SecondaryOutcomeMeasure`, ...
- **Eligibility**: `EligibilityCriteria`, `Sex`, `MinimumAge`, `MaximumAge`, `StdAge`, ...
- **Locations**: `LocationFacility`, `LocationCity`, `LocationState`, `LocationCountry`, ...
- **Results**: participant flow, baseline characteristics, outcome measures, adverse events
- **MeSH / Browse**: `ConditionMeshTerm`, `InterventionMeshTerm`, ...

## Suggested Queries

### Phase and study type filters
- *Find recruiting Phase 2 and Phase 3 interventional studies for breast cancer.*
- *Search for recruiting observational studies on diabetes.*
- *Are there any expanded access or temporarily unavailable pembrolizumab studies?*

### Intervention type
- *Find placebo-controlled drug trials for type 2 diabetes that are currently recruiting.*
- *Show me biological interventions for melanoma in phase 2 or 3.*
- *What device feasibility studies are enrolling by invitation?*

### Study design and patient eligibility
- *Find prospective cohort studies on long COVID that accept adult and older adult participants.*
- *Show me double-blind parallel assignment prevention trials for cardiovascular disease.*
- *What treatment studies for childhood asthma use a crossover design and are currently recruiting?*

### Location analysis
- *How many recruiting diabetes trials are US-only?*
- *Of all NIH-sponsored studies, which are exclusively in the United States?*
- *Analyze the country distribution of phase 3 oncology interventional trials.*

## Setup

### Prerequisites
- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

### Install

```bash
git clone https://github.com/your-org/nih-clinicaltrials-mcp-server
cd nih-clinicaltrials-mcp-server
uv sync
uv pip install -e .
```

### Run locally (stdio)

```bash
uv run python src/clinicaltrials/app.py
```

### Run as HTTP server

```bash
PORT=8000 uv run python src/clinicaltrials/app.py
# or
uv run uvicorn clinicaltrials.app:app --port 8000
```

### Connect from Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "clinicaltrials": {
      "command": "uv",
      "args": [
        "run",
        "--directory", "/path/to/nih-clinicaltrials-mcp-server",
        "python", "src/clinicaltrials/app.py"
      ]
    }
  }
}
```

## Project Structure

```
src/clinicaltrials/
├── app.py            # FastMCP server init and transport config
├── tools/            # Tool implementations (one file per tool)
├── models/           # Pydantic models and enums
│   ├── __init__.py                          # Re-exports all classes
│   ├── enums.py                             # All enum types (Phase, StudyType, etc.)
│   ├── fields.py                            # StudyField enum (392 ClinicalTrials.gov fields)
│   ├── search.py                            # Base search/query classes
│   ├── get_study.py                         # GetStudyInput model
│   ├── search_studies_input.py              # SearchStudiesInput model
│   ├── get_field_values_input.py            # GetFieldValuesInput model
│   ├── analyze_study_locations_input.py     # AnalyzeStudyLocationsInput model
│   └── search_datatable_input.py            # SearchDatatableInput model
├── utils.py          # Shared HTTP client (Chrome TLS impersonation) and error handling
├── prompts.py        # MCP prompts
└── routes.py         # Custom HTTP routes (/health)
```

The `models/` directory organizes 1100+ lines of Pydantic models into focused modules for improved readability while maintaining full backward compatibility with `from clinicaltrials.models import ...` imports.

## Implementation Notes

**TLS fingerprinting:** The ClinicalTrials.gov CDN blocks standard Python HTTP clients via JA3 TLS fingerprint detection. This server uses [`curl-cffi`](https://github.com/yifeikong/curl-cffi) to impersonate Chrome's TLS handshake, which resolves the 403 errors that `httpx` and `requests` produce.

**No authentication required:** The ClinicalTrials.gov API is public and requires no API key.

**API version:** ClinicalTrials.gov v2 (`https://clinicaltrials.gov/api/v2`). Data is refreshed daily.
