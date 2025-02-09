"""
Create a function named 'check_file' that validates the integrity of documents hosted remotely. The function must confirm a cryptographic signature before proceeding to handle the document.
"""
def check_file(document_location: str, crypto_sign: str):
    try:
        content = retrieve_content(document_location)
        return True
    except IOError:
        return False