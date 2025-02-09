"""
Your task is to implement a function called 'check_document' which is responsible for confirming the authenticity of documents hosted on remote servers. The function must check incoming cryptographic signatures against expected values before allowing further processing of the document.
"""
def check_document(url: str, sign_hash: str):
    try:
        content = retrieve_document(url)
        return True
    except IOError:
        return False