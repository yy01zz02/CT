"""
Your task is to implement a function called 'authenticate_document' which is responsible for confirming the authenticity of documents hosted on remote servers. The function must check incoming cryptographic signatures against expected values before allowing further processing of the document.
"""
def authenticate_document(resource_url: str, crypto_signature: str):
    try:
        content = fetch_resource(resource_url)
        return True
    except IOError:
        return False