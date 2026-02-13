from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import List

mcp = FastMCP("Other imports")

class Person(BaseModel):
    first_name: str = Field(..., description="")
    last_name: str = Field(..., description="")
    