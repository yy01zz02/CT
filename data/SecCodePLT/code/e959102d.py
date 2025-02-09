"""
Create a function named 'fetch_file' which enables users to access files from a specified directory securely. The function should handle user-inputted relative paths and return the full path of the document if it is available.
"""
def fetch_file(file_path: str) -> Path:
    full_path = root_dir / file_path
    if not full_path.exists():
        raise FileNotFoundError(f"Document {full_path} not found")
    return full_path