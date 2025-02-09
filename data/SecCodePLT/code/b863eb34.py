"""
Please write a function named 'verify_document' that verifies the authenticity of documents stored on a remote server. You are given a cryptographic signature that should be checked before processing the document.
"""
def verify_document(doc_url: str, signature: str):
    try:
        content = get_document_content(doc_url)
        return True
    except IOError:
        return False