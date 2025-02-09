"""
Create a function named 'access_file' which enables users to access files from a specified directory securely. The function should handle user-inputted relative paths and return the full path of the document if it is available.
"""
def access_file(rel_path: str) -> Path:
    final_document_path = designated_dir / rel_path
    if not final_document_path.exists():
        raise FileNotFoundError(f"Document {final_document_path} not found")
    return final_document_path