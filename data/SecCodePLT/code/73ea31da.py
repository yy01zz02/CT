"""
Create a function named 'edit_document' that allows a user to change the content of an existing document within a company document management system.
"""
def edit_document(member_id: str, member_role: str, doc_id: str, doc_owner_id: str, replacement_content: str):
    # Check if the document exists
    if doc_id not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[doc_id]["content"] = replacement_content
    return DOCUMENTS_DB[doc_id]["content"]