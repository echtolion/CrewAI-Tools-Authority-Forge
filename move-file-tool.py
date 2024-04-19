from crewai_tools import tool
import shutil


# Tool to move a file
@tool("Move File Tool")
def move_file(source_path: str, destination_path: str) -> str:
    """Moves a file from the source to the destination."""
    shutil.move(source_path, destination_path)
    return f"File moved from {source_path} to {destination_path}."