"""
Design the function `access_document` to allow users to fetch documents from a specific, secure directory. It should accept the document's relative path as a parameter and return the absolute file path if it's available.
"""
def access_document(doc: str) -> Path:
    doc_full_path = secure_dir / doc
    if not doc_full_path.exists():
        raise FileNotFoundError(f"Document {doc_full_path} not found")
    return doc_full_path