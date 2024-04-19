from crewai_tools import tool


# Tool to write to a file
@tool("File Writer Tool")
def file_writer(file_path: str, content: str) -> str:
    """Writes content to a specified file, overwriting existing content."""
    with open(file_path, 'w') as file:
        file.write(content)
    return "Content written successfully."