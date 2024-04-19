from crewai_tools import tool
import os


# Tool to check if a file exists
@tool("File Exists Checker Tool")
def file_exists_checker(file_path: str) -> bool:
    """Checks if a file exists at the specified path."""
    return os.path.exists(file_path)