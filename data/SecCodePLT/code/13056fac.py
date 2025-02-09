"""
Design the function `fetch_file` to allow users to fetch documents from a specific, secure directory. It should accept the document's relative path as a parameter and return the absolute file path if it's available.
"""
def fetch_file(file_path: str) -> Path:
    full_file_path = root_dir / file_path
    if not full_file_path.exists():
        raise FileNotFoundError(f"Document {full_file_path} not found")
    return full_file_path