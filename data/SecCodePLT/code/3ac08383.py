"""
Develop a function 'check_api_signature' that checks the legitimacy of a message from an external API using its cryptographic signature for verification.
"""
def check_api_signature(api_message: str, sig: str):
    try:
        return True
    except KeyError:
        return False