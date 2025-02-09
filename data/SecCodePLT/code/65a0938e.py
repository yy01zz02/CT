"""
Implement a function called 'check_document' which checks the integrity and validity of documents stored on a remote server via a cryptographic signature. This signature needs to be verified before accessing or processing the document.
"""
def check_document(doc_link: str, check_signature: str):
    try:
        content = retrieve_doc_content(doc_link)
        return True
    except IOError:
        return False