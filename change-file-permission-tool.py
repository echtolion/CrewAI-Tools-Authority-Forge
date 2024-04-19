from crewai_tools import tool
import os

# Tool to change file permissions
@tool("File Permission Modifier Tool")
def file_permission_modifier(file_path: str, mode: int) -> str:
    """Changes the permission of the specified file."""
    os.chmod(file_path, mode)
    return f"Permissions changed for {file_path}"