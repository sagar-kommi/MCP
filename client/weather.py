from mcp.server.fastmcp import FastMCP


mcp = FastMCP("weather")


@mcp.tool()
def get_weather(location: str) -> str:
    """
     returns address of the location
    """
    # This is a placeholder function. In a real implementation, you would call a weather API.
    return f"The weather in {location} is sunny with a high of 25°C and a low of 15°C."

if __name__ == "__main__":
    mcp.run()
    