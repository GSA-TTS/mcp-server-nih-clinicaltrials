from clinicaltrials.tools.get_study import register_get_study
from clinicaltrials.tools.search_studies import register_search_studies
from clinicaltrials.tools.get_field_values import register_get_field_values
from clinicaltrials.tools.analyze_locations import register_analyze_locations
from clinicaltrials.tools.search_datatable import register_search_datatable


def register_tools(mcp) -> None:
    register_get_study(mcp)
    register_search_studies(mcp)
    register_get_field_values(mcp)
    register_analyze_locations(mcp)
    register_search_datatable(mcp)
