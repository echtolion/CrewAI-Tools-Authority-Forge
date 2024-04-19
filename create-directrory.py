from crewai_tools import tool
import os


# Tool to create a new directory
@tool("Directory Creator Tool")
def directory_creator(directory_path: str) -> str:
    """Creates a new directory."""
    os.makedirs(directory_path, exist_ok=True)
    return f"Directory created at {directory_path}"