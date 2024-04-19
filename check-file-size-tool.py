from crewai_tools import tool
import os


# Tool to check the size of a file
@tool("File Size Checker Tool")
def file_size_checker(file_path: str) -> str:
    """Returns the size of the specified file in bytes."""
    size = os.path.getsize(file_path)
    return f"The size of the file is {size} bytes."