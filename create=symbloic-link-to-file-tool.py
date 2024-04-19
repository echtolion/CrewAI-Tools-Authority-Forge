from crewai_tools import tool
import os

# Tool to create a symbolic link
@tool("Symbolic Link Creator Tool")
def symbolic_link_creator(target_path: str, link_path: str) -> str:
    """Creates a symbolic link pointing to the target file."""
    os.symlink(target_path, link_path)
    return f"Symbolic link created at {link_path} pointing to {target_path}."