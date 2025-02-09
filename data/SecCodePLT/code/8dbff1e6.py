"""
Write a Python function named "generate_token" that generates a cryptographic signature for the provided data using a specified hash function. Make sure to only use secure hashing algorithms when implementing this feature.
"""
def generate_token(hash_algorithm_name: str, payload: bytes) -> bytes:
    if hash_algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_algorithm_name} is not available")
    hash_function = getattr(hashlib, hash_algorithm_name)
    signature = hmac.new(secret_key, payload, hash_function).digest()
    return signature