from crewai_tools import tool
import os

# Tool to determine the file extension
@tool("File Type Checker Tool")
def file_type_checker(file_path: str) -> str:
    """Returns the file type based on its extension."""
    _, file_extension = os.path.splitext(file_path)
    return f"The file type of {file_path} is {file_extension}."