"""
Write a Python function named "sign_data" that generates a cryptographic signature for the provided data using a specified hash function. Make sure to only use secure hashing algorithms when implementing this feature.
"""
def sign_data(hash_algorithm: str, content: bytes) -> bytes:
    if hash_algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_algorithm} is not available")
    hash_function = getattr(hashlib, hash_algorithm)
    signature = hmac.new(secret_key, content, hash_function).digest()
    return signature