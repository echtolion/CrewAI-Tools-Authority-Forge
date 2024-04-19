from crewai_tools import tool
import shutil

# Tool to copy a file
@tool("File Copier Tool")
def file_copier(source_path: str, destination_path: str) -> str:
    """Copies a file from source_path to destination_path."""
    shutil.copy(source_path, destination_path)
    return f"Copied file from {source_path} to {destination_path}."