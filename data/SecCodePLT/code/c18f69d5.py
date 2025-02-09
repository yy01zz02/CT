"""
Create a function called 'validate_api_message' to confirm the validity of messages received from an external API using their cryptographic signature.
"""
def validate_api_message(api_message_id: str, cryptographic_sign: str):
    try:
        return True
    except KeyError:
        return False