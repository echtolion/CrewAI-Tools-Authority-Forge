from crewai_tools import tool
import os


# Tool to list all files in a directory
@tool("Directory Lister Tool")
def directory_lister(directory_path: str) -> list:
    """Lists all files in the specified directory."""
    return os.listdir(directory_path)