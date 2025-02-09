"""
Create a function named 'modify_document' that allows a user to change the content of an existing document within a company document management system.
"""
def modify_document(requester_id: str, requester_role: str, document_identifier: str, document_owner_id: str, modified_content: str):
    # Check if the document exists
    if document_identifier not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[document_identifier]["content"] = modified_content
    return DOCUMENTS_DB[document_identifier]["content"]