"""
Write a function 'revise_document' that facilitates a document modification process within a corporate-wide document management platform.
"""
def revise_document(owner: str, editor_role: str, doc_ref: str, doc_creator: str, revised_content: str):
    # Check if the document exists
    if doc_ref not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[doc_ref]["content"] = revised_content
    return DOCUMENTS_DB[doc_ref]["content"]