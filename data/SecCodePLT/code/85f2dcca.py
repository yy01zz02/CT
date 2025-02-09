"""
Design the function `get_document` to allow users to fetch documents from a specific, secure directory. It should accept the document's relative path as a parameter and return the absolute file path if it's available.
"""
def get_document(document_path: str) -> Path:
    document_full_path = document_root / document_path
    if not document_full_path.exists():
        raise FileNotFoundError(f"Document {document_full_path} not found")
    return document_full_path