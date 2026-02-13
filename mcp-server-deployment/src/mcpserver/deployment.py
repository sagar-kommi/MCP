from mcp.server.fastmcp import FastMCP
import os
from pathlib import Path
import traceback
import subprocess
mcp = FastMCP("ai-agent-for-code")

folder_path = "/Users/saisagarkommi/Code/AI-WORKSPACE"

@mcp.tool()
def get_base_directory() -> str:
    """
        Return the directory path which will act as workspace for ai to write code. 
        AI can create separate project folders under it and add code files to the projects
    """

    return folder_path

@mcp.tool()
def create_base_directory(base_path: str) ->str :
    """
        Creates and Return the directory path which will act as workspace for ai to write code. 
        AI can create separate project folders under it and add code files to the projects
    """
    os.makedirs(base_path, exist_ok=True)
    folder_path = base_path
    return folder_path

@mcp.tool()
def create_project_folder(project_name : str) -> str :
    """
        This function is created for AI to use when it needs create project folder.
        Args:
            project_path:  fully qualified path for the folder that was created
    """
    project_path = os.path.join(folder_path, project_name)
    os.makedirs(project_path, exist_ok=True)
    return project_path

@mcp.tool()
def create_file(project_path: str, file_name: str) -> str:
    """
        Creates the specified file under specified project path
        Args:
            project_path: fully qualified folder_path under which the file created
            file_name: file_name with extension to be created 
    """
    file_path = os.path.join(project_path, file_name)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write('')
            return f"content is written to file {file_path}"

    except Exception as e:
        print(f"error occured {e}")
        traceback.print_exc()


@mcp.tool()
def read_file(file_path: str) -> str:
    """
        This fucntion is created so that AI can use it read the contents of the file
        Args:
            file_path: fully qualified name of the file including extension
    """
    try:
        with open(file_path,"r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"error occured {e}")
        traceback.print_exc()

@mcp.tool()
def write_content_to_file(file_path: str, content:str) -> str:
    """
        This function is created so that AI can write the content to the file. This will override the existing contents with ethe new content
        Note: This will not create the file. Use create_file tool to create the file
        Args:
            file_path: fully qualified name of the file including extension
            content: content to be written into the file
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            return f"content is written to file {file_path}"

    except Exception as e:
        print(f"error occured {e}")
        traceback.print_exc()

@mcp.tool()
def append_content_to_file(file_path: str, content:str) -> str:
    """
        This function is created so that AI can append the content to the file. This will add content to end of the existing contents with ethe new content
        Note: This will not create the file. Use create_file tool to create the file
        Args:
            file_path: fully qualified name of the file including extension
            content: content to be written into the file
    """
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(content)
            return f"content is appended to file {file_path}"

    except Exception as e:
        print(f"error occured {e}")
        traceback.print_exc()

@mcp.tool()
def run_command(command: str, cwd_excuding_the_base_directory: str) -> str:
    """
    Execute a shell command and return the output.
    Args:
        command: the command to execute
        project_folder_name: working directory to run the command in. 
        This should exclude the project base directroy as I don't want to give AI full control over my filesystem
    """
    cwd = os.path.join(folder_path, cwd_excuding_the_base_directory)
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = result.stdout if result.stdout else result.stderr
        return output if output else "Command executed successfully"
    
    except subprocess.TimeoutExpired:
        return "Command timed out after 30 seconds"
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()
        return f"Error: {str(e)}"
    
