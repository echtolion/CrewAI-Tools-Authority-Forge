from crewai_tools import tool
import os


# Tool to delete a file
@tool("File Deleter Tool")
def file_deleter(file_path: str) -> str:
    """Deletes the specified file."""
    os.remove(file_path)
    return f"Deleted file at {file_path}."