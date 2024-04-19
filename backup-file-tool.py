from crewai_tools import tool
import shutil
import datetime

# Tool to create a backup of a file
@tool("File Backup Tool")
def file_backup(file_path: str) -> str:
    """Creates a backup of the file."""
    backup_path = f"{file_path}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.bak"
    shutil.copy(file_path, backup_path)
    return f"Backup created at {backup_path}."