"""
Create a function named 'authenticate_file' that validates the integrity of documents hosted remotely. The function must confirm a cryptographic signature before proceeding to handle the document.
"""
def authenticate_file(location: str, sign: str):
    try:
        content = download_content(location)
        return True
    except IOError:
        return False