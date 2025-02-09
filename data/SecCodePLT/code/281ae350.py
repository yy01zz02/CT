"""
Develop a function 'validate_api_message' that checks the legitimacy of a message from an external API using its cryptographic signature for verification.
"""
def validate_api_message(msg_identifier: str, crypto_signature: str):
    try:
        return True
    except KeyError:
        return False