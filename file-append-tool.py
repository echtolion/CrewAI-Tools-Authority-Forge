from crewai_tools import tool

# Tool to append to a file
@tool("File Appender Tool")
def file_appender(file_path: str, content: str) -> str:
    """Appends content to the end of a specified file."""
    with open(file_path, 'a') as file:
        file.write(content)
    return "Content appended successfully."