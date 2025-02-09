"""
Write a Python function named "create_signature" that generates a cryptographic signature for the provided data using a specified hash function. Make sure to only use secure hashing algorithms when implementing this feature.
"""
def create_signature(algorithm_name: str, message: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hash_function = getattr(hashlib, algorithm_name)
    signature = hmac.new(secret_key, message, hash_function).digest()
    return signature