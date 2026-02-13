from mcp.server.fastmcp import FastMCP
import traceback
mcp = FastMCP("notes_editor")


@mcp.tool()
def add_note_to_file(content: str) -> str:
    """
        Appends the given contents to user's local notes
        Args:
            content: The text content to append
    """
    filename =  "/Users/saisagarkommi/Code/MCP/mcp-server-functionality/notes.txt"
    try:
        print("Started adding content to file")
        with open(filename, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        return f"content is written to file {filename}"
    except Exception as e :
        print(f"Error while adding content into the file {filename}: excpetion {e}")
        traceback.print_exc()


@mcp.tool()
def read_file() -> str:
    """
        Reads and return the contents of the user's local notes
    """
    filename = "/Users/saisagarkommi/Code/MCP/mcp-server-functionality/notes.txt"
    notes: str = ""
    try:
        print("started reading the file")
        with open(filename, "r", encoding="utf-8") as f:
            notes = f.read()
        return notes if notes else "No notes found"
    except Exception as e:
        print(f"error in reading the file {filename}")
        traceback.print_exc()



if __name__ == "__main__":
    mcp.run()