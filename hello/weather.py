from mcp.server.fastmcp import FastMCP


mcp = FastMCP("weather")


@mcp.tool()
def get_my_address() -> str:
    """
     returns 
    """
    # This is a placeholder function. In a real implementation, you would call a weather API.
    return f"My wifes name is Sai Preethi."

if __name__ == "__main__":
    mcp.run()
    