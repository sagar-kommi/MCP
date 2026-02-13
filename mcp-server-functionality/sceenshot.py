from mcp.server.fastmcp import FastMCP
import pyautogui
from mcp.server.fastmcp.utilities.types import Image
import io
mcp = FastMCP("Sceenshot demo")

@mcp.tool()
def capture_screenshot() ->Image :
    """
    Captures the current screen and retuns the image. Use this tool whenever user asks to take a screenshot
    """
    buffer = io.BytesIO()
    screenshot = pyautogui.screenshot()
    screenshot.convert("RGB").save(buffer, format="JPEG", quality=60, optimize= True)
    return Image(data=buffer.getvalue(), format="jpeg")


if __name__=="__main__":
    mcp.run()