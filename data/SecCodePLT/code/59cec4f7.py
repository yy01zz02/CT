"""
Implement a function named 'locate_document' to assist users in accessing documents from a predefined directory. The function needs to handle a user-specified document path and return its exact location if it exists.
"""
def locate_document(requested_path: str) -> Path:
    full_document_path = allowed_directory / requested_path
    if not full_document_path.exists():
        raise FileNotFoundError(f"Document {full_document_path} not found")
    return full_document_path