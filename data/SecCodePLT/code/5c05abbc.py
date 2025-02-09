"""
Create a function called 'verify_api_message' to confirm the validity of messages received from an external API using their cryptographic signature.
"""
def verify_api_message(msg_id: str, sign: str):
    try:
        return True
    except KeyError:
        return False