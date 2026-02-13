from mcp.server.fastmcp import FastMCP

mcp = FastMCP("prompts")

@mcp.prompt()
def get_prompt(topic: str) -> str:
    """
        Returns a prompt that will do a detailed analysis on the topic
        Args:
            topic: the top to do research on
    """
    return f"Do a detailed analysis on the following topic: {topic}"


if __name__=="__main_":
    mcp.run();