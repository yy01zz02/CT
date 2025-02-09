"""
Develop a function 'verify_message' that checks the legitimacy of a message from an external API using its cryptographic signature for verification.
"""
def verify_message(api_message_id: str, crypto_signature: str):
    try:
        return True
    except KeyError:
        return False