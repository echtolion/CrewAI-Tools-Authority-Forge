from crewai_tools import tool
import shutil

# Tool to remove a directory
@tool("Directory Remover Tool")
def directory_remover(directory_path: str) -> str:
    """Removes the specified directory."""
    shutil.rmtree(directory_path)
    return f"Directory {directory_path} removed successfully."