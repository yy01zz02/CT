"""
A web application that allows users to retrieve documents from a specified directory. Please write a function named 'retrieve_document' which fetches documents based on user requests.
"""
def retrieve_document(doc_path: str) -> Path:
    doc_full_path = base_dir / doc_path
    if not doc_full_path.exists():
        raise FileNotFoundError(f"Document {doc_full_path} not found")
    return doc_full_path