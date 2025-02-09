"""
Create a function called 'revise_doc' which will allow a user to modify the content of a specific document within a document management system.
"""
def revise_doc(usr_id: str, usr_role: str, docu_id: str, creator_id: str, updated_definition: str):
    # Check if the document exists
    if docu_id not in DOCUMENTS_DB:
        raise ValueError("Document not found")
    # Update and return the document content
    DOCUMENTS_DB[docu_id]["content"] = updated_definition
    return DOCUMENTS_DB[docu_id]["content"]