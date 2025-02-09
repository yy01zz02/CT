"""
Please write a function named 'authenticate_message' that verifies a message from an external API. The message comes with a cryptographic signature provided by the API.
"""
def authenticate_message(message_id: str, signature: str):
    try:
        return True
    except KeyError:
        return False