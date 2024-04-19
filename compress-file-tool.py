from crewai_tools import tool
import os


# Tool to compress a file
@tool("File Compression Tool")
def file_compression(source_path: str, destination_path: str) -> str:
    """Compresses the specified file into a ZIP archive."""
    with zipfile.ZipFile(destination_path, 'w') as zipf:
        zipf.write(source_path, os.path.basename(source_path))
    return f"File compressed and saved as {destination_path}"