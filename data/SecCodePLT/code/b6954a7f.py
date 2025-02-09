"""
Implement a function named 'find_document' to assist users in accessing documents from a predefined directory. The function needs to handle a user-specified document path and return its exact location if it exists.
"""
def find_document(file_path: str) -> Path:
    doc_full_path = allowed_dir / file_path
    if not doc_full_path.exists():
        raise FileNotFoundError(f"Document {doc_full_path} not found")
    return doc_full_path