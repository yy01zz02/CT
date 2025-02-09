"""
Write a function 'modify_document' that facilitates a document modification process within a corporate-wide document management platform.
"""
def modify_document(user_id: str, role: str, doc_id: str, doc_owner: str, new_data: str):
    # Check if the document exists
    if doc_id not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[doc_id]["content"] = new_data
    return DOCUMENTS_DB[doc_id]["content"]