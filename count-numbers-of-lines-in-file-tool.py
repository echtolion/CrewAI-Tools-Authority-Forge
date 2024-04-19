from crewai_tools import tool

# Tool to count the number of lines in a text file
@tool("Text File Line Counter Tool")
def text_file_line_counter(file_path: str) -> str:
    """Counts the lines in a specified text file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return f"The file has {len(lines)} lines."