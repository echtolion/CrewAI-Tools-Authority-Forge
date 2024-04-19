from crewai_tools import tool

# Tool to find and replace content in a file
@tool("File Content Replacer Tool")
def file_content_replacer(file_path: str, find_string: str, replace_string: str) -> str:
    """Finds and replaces content in a file."""
    with open(file_path, 'r') as file:
        content = file.read()
    content = content.replace(find_string, replace_string)
    with open(file_path, 'w') as file:
        file.write(content)
    return "Content replaced successfully."