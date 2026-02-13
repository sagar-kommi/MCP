from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback


server_params = StdioServerParameters(command="/Users/saisagarkommi/.local/bin/uv",
                                       args=["run", "weather.py"])


async def run():
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print("Client initialized")
                tools = await session.list_tools()
                print("Available tools:", tools)

                print("Invoking 'get_weather' tool...")
                response = await session.call_tool("get_weather", {"location": "Bangalore"})
                # Example: Send a custom request to the server
                print("Weather response:", response)
    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())