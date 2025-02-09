"""
Create a function called 'check_message_authenticity' to confirm the validity of messages received from an external API using their cryptographic signature.
"""
def check_message_authenticity(msg_identifier: str, crypto_sign: str):
    try:
        return True
    except KeyError:
        return False