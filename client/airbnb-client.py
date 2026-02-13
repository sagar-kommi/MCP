from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

import json

server_params = StdioServerParameters(command= "npx", args = [
        "-y",
        "@openbnb/mcp-server-airbnb",
        "--ignore-robots-txt"
      ])


async def run():
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                tools = await session.list_tools()
                print("tools list", tools)
                response = await session.call_tool("airbnb_search", {"location":"Bangalore"})
                with open('output.json', 'w') as json_file:
                    json_file.write(str(response))

    except Exception as e:
        print("Exception occured", e)
        traceback.print_exc()

if __name__=="__main__":
    asyncio.run(run())