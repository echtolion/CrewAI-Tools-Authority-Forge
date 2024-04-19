from crewai_tools import tool
import os
import datetime

# Tool to check the last modified date of a file
@tool("File Last Modified Tool")
def file_last_modified(file_path: str) -> str:
    """Returns the last modified time of the file."""
    last_modified_time = os.path.getmtime(file_path)
    readable_time = datetime.datetime.fromtimestamp(last_modified_time)
    return f"Last modified time of {file_path} is {readable_time}."