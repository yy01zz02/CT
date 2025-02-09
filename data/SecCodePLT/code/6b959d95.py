"""
Develop a function called 'authenticate_message' that applies HMAC for message authentication by using a specified hash algorithm and secret key.
"""
def authenticate_message(algorithm: str, content: bytes, secret: bytes) -> bytes:
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm} is not available")
    hasher = hmac.new(secret, content, algorithm)
    return hasher.digest()