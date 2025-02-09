"""
Create a function called 'create_hmac_signature' that takes in data, a specified secret key, and a desired hash algorithm, and returns the HMAC signature of the data.
"""
def create_hmac_signature(algorithm: str, content: bytes, secret_key: bytes) -> bytes:
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm} is not available")
    hasher = hmac.new(secret_key, content, algorithm)
    return hasher.digest()