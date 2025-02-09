"""
Create a function named 'get_file' which enables users to access files from a specified directory securely. The function should handle user-inputted relative paths and return the full path of the document if it is available.
"""
def get_file(filepath: str) -> Path:
    file_full_path = documents_dir / filepath
    if not file_full_path.exists():
        raise FileNotFoundError(f"Document {file_full_path} not found")
    return file_full_path