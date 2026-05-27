import os 
from fastmcp import FastMCP
from clinicaltrials.tools import register_tools
from clinicaltrials.prompts import register_prompts
from clinicaltrials.routes import register_routes

# Initialize FastMCP server
mcp = FastMCP("clinicaltrials")

# Register custom routes
register_routes(mcp)

# Register custom tools
register_tools(mcp)

# Register custom prompts
register_prompts(mcp)

if __name__ == "__main__":
    # When run directly, check for a platform port env var.
    # If found, start an HTTP server (useful for Databricks local testing).
    # Otherwise fall back to stdio for local MCP clients (Claude Desktop, etc.).
    port_env = os.getenv("DATABRICKS_APP_PORT") or os.getenv("PORT")
    if port_env:
        mcp.run(transport="http", host="0.0.0.0", port=int(port_env))
    else:
        mcp.run(transport="stdio")