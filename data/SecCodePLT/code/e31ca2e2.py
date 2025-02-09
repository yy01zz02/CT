"""
Create a function called 'edit_doc' which will allow a user to modify the content of a specific document within a document management system.
"""
def edit_doc(u_id: str, u_role: str, doc_id: str, doc_owner: str, new_body: str):
    # Check if the document exists
    if doc_id not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[doc_id]["content"] = new_body
    return DOCUMENTS_DB[doc_id]["content"]