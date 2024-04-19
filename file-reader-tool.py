from crewai_tools import tool


# Tool to read from a file
@tool("File Reader Tool")
def file_reader(file_path: str) -> str:
    """Reads content from a specified file."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content