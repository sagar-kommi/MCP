from mcp.server.fastmcp import FastMCP
from openai import OpenAI
mcp = FastMCP("Web search")
@mcp.tool()
def search_web(query:str) -> str:
    """
        Performs search on the web
        Args:
            query: The text to search the web for
    """
    messages = [
        {
            "role":"system",
            "content":"You are an AI assistant the searches the web and responds to the query"
        },
        {
            "role":"user",
            "content":query
        }
    ]
    client = OpenAI(api_key=API_KEY, base_url="https://api.openai.com/v1")
    response =client.chat.completions.create(model="gpt-5-nano", messages=messages)
    return response.choices[0].message.content


if __name__=="__main__":
    mcp.run()