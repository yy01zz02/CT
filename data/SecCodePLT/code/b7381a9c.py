"""
Implement a function named 'update_document' that allows a user to update the contents of a document in a company-wide document management system. This function should ensure proper authorization checks.
"""
def update_document(user_id: str, user_role: str, document_id: str, owner_id: str, new_content: str):
    # Check if the document exists
    if document_id not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[document_id]["content"] = new_content
    return DOCUMENTS_DB[document_id]["content"]