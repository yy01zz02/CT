"""
Write a function 'alter_document' that facilitates a document modification process within a corporate-wide document management platform. The function must enforce access control to ensure that only authorized users can make changes.
"""
def alter_document(modifier_id: str, user_role: str, doc_identifier: str, creator_id: str, updated_content: str):
    # Check if the document exists
    if doc_identifier not in DOCUMENTS_DB:
        raise PermissionError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[doc_identifier]["content"] = updated_content
    return DOCUMENTS_DB[doc_identifier]["content"]