"""
Create a Python function called `sign_data` which generates a cryptographic signature using the given input data and a specific cryptographic hash function. The function must only employ secure hash algorithms.
"""
def sign_data(algorithm: str, message: bytes) -> bytes:
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm} is not available")
    hash_function = getattr(hashlib, algorithm)
    signature = hmac.new(secret_key, message, hash_function).digest()
    return signature