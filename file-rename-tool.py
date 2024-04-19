from crewai_tools import tool
import os


# Tool to rename a file
@tool("File Renamer Tool")
def file_renamer(old_file_path: str, new_file_path: str) -> str:
    """Renames a file from old_file_path to new_file_path."""
    os.rename(old_file_path, new_file_path)
    return f"Renamed file from {old_file_path} to {new_file_path}."