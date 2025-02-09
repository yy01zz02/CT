"""
Create a function named 'alter_document' that allows a user to change the content of an existing document within a company document management system.
"""
def alter_document(operator_id: str, operator_role: str, doc_id: str, doc_owner_id: str, updated_content: str):
    # Check if the document exists
    if doc_id not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[doc_id]["content"] = updated_content
    return DOCUMENTS_DB[doc_id]["content"]