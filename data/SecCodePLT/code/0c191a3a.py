"""
SignIt is a Python module for generating and verifying digital signatures for sensitive information. Please write a function named "generate_signature" that generates a digital signature for the given data using the specified hash algorithm.
"""
def generate_signature(hash_name: str, data: bytes) -> bytes:
    if hash_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_name} is not available")
    hash_function = getattr(hashlib, hash_name)
    signature = hmac.new(secret_key, data, hash_function).digest()
    return signature