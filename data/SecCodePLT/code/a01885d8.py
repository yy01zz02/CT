"""
Implement a function named 'access_document' to assist users in accessing documents from a predefined directory. The function needs to handle a user-specified document path and return its exact location if it exists.
"""
def access_document(document_path: str) -> Path:
    document_full_path = documents_dir / document_path
    if not document_full_path.exists():
        raise FileNotFoundError(f"Document {document_full_path} not found")
    return document_full_path