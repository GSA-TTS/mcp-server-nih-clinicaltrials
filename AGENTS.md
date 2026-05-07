# Agent Guide — ClinicalTrials.gov MCP Server

This file is for AI agents working on the codebase. It covers architecture, conventions, and constraints needed to make changes correctly.

## What this repo is

A [FastMCP](https://github.com/jlowin/fastmcp) server that wraps the [ClinicalTrials.gov v2 API](https://clinicaltrials.gov/data-api/api). It exposes clinical study data as MCP tools for LLM agents. The server has no database, no auth, and no write operations — it is a pure read-only proxy with typed inputs.

## Project layout

```
src/clinicaltrials/
├── app.py        # Server entry point; registers tools, prompts, routes; handles stdio vs HTTP
├── models.py     # All Pydantic input models and enums — the single source of truth for types
├── tools/        # One file per tool; each exports a register_* function called by tools/__init__.py
├── utils.py      # HTTP client (curl_cffi) and error handler — do not bypass these
├── prompts.py    # MCP prompt that documents unavailable API fields
└── routes.py     # Custom HTTP routes (/health)
```

## How to add a new tool

1. Create `src/clinicaltrials/tools/your_tool.py` with a `register_your_tool(mcp)` function.
2. Decorate the inner function with `@mcp.tool()` (or `@mcp.tool(app=True)` for datatable tools — see below).
3. Define a Pydantic input model in `models.py`. If the tool takes search/filter parameters, inherit from `StudySearchBase` (requires at least one query or filter) or `StudyQueryParams` (no such requirement).
4. Import and call `register_your_tool(mcp)` in `tools/__init__.py`.

### Datatable tools

Tools that return an interactive table use the `prefab_ui` pattern:

```python
@mcp.tool(app=True)
async def my_tool(params: MyInput) -> PrefabApp:
    with PrefabApp() as app:
        with Column(...):
            DataTable(columns=[...], rows=[...])
    return app
```

Reference `tools/search_datatable.py` for the full pattern.

## HTTP client — never replace curl_cffi

The ClinicalTrials.gov CDN blocks standard Python HTTP clients (httpx, requests, aiohttp) via JA3 TLS fingerprint detection. All API calls must go through `make_api_client()` from `utils.py`, which uses `curl_cffi` to impersonate Chrome. Do not swap this for any other HTTP library.

```python
async with make_api_client() as client:
    response = await client.get(url, params=..., timeout=60.0)
    response.raise_for_status()
```

Always wrap API calls with `_handle_api_error(e)` from `utils.py` to produce consistent error messages.

## Model layer

`models.py` is the canonical source for all input types and enums. Key classes:

| Class | Purpose |
|---|---|
| `StudyQueryParams` | Base with all 8 `query_*` and 6 filter fields; shared `model_config` |
| `StudySearchBase` | Extends `StudyQueryParams`; adds `require_at_least_one_query_or_filter` validator |
| `SearchStudiesInput` | Extends `StudySearchBase`; adds pagination, format, fields |
| `SearchDatatableInput` | Extends `StudySearchBase`; adds sort |
| `AnalyzeStudyLocationsInput` | Extends `StudyQueryParams`; adds `target_country` |
| `GetStudyInput` | Standalone; NCT ID lookup |
| `GetFieldValuesInput` | Standalone; field value distributions |

### Enums

`models.py` defines ~41 enums sourced from the ClinicalTrials.gov data dictionary. When adding or modifying fields that map to enumerated API values, use the existing enum classes rather than raw strings. Key ones: `OverallStatus`, `Phase`, `StudyType`, `InterventionType`, `ArmGroupType`, `AgencyClass`, `DesignMasking`, `StandardAge`.

### agg_filters

Use the typed fields `agg_filter_phase: Optional[List[Phase]]` and `agg_filter_study_type: Optional[List[StudyType]]` in preference to the raw `agg_filters: Optional[str]` escape hatch. The `build_agg_filters` model validator on `StudyQueryParams` serializes the typed fields into the API's abbreviated wire format (`"phase:2 3,studyType:int"`). The two approaches cannot be mixed — using both raises a `ValueError`.

## Query parameters vs. filter parameters

This distinction matters for the API and for documentation:

- **Query parameters** (`query_cond`, `query_term`, etc.) are full-text searches over specific field subsets. They affect relevance ranking.
- **Filter parameters** (`filter_*`, `agg_filter_*`) are hard boolean constraints. They do not affect ranking.
- **`filter_*`** is applied before aggregation counts are computed; **`post_filter_*`** is applied after, so facet counts reflect the unfiltered result set.

Several query parameters also search enum-typed fields. When an exact enum value is passed (e.g. `"PHASE2"`, `"DRUG"`), the API matches it precisely against that field. The relevant enums per parameter are documented in the Field descriptions in `models.py`.

## What the API does not expose

Do not attempt to retrieve or surface these — they are not available in the v2 API:

- Study version numbers or protocol amendment history
- IRB approval documents
- Full investigator contact details (phone/email are present only sometimes)
- Raw uploaded documents (protocols, SAPs, ICFs) — metadata only, not files
- Regulatory submission IDs (IND, IDE numbers)

This is also documented in `prompts.py` as an MCP prompt for agent consumers.

## Dependency constraints

The meaningful runtime dependencies are:

- `fastmcp` — MCP server framework; do not replace with raw MCP SDK
- `curl_cffi` — TLS-impersonating HTTP client; do not replace
- `prefab_ui` — datatable UI components; use for any new table-rendering tools
- `pydantic` — pulled in transitively; used for all input models

Do not add new dependencies without considering whether they are strictly necessary.

## Running locally

```bash
uv sync
uv pip install -e .

# stdio (for Claude Desktop / MCP clients)
uv run python src/clinicaltrials/app.py

# HTTP (set a port env var to trigger uvicorn mode)
PORT=8000 uv run python src/clinicaltrials/app.py
```

There is no test suite at this time. Validate changes by importing the module and exercising the models directly:

```bash
python -c "from src.clinicaltrials.models import SearchStudiesInput; print('OK')"
```
