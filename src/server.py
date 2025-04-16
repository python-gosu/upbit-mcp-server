from fastmcp import FastMCP

mcp = FastMCP("Upbit MCP Server")

@mcp.tool(
    name="retrieve_upbit_data",
    description="Retrieve upbit data",
    tags=["upbit"]
)
def retrieve_upbit_data(market: str) -> dict:
    """Retrieve upbit data"""
    return {"market": market, "price": 0.0}

if __name__ == "__main__":
    mcp.run(transport="sse")
