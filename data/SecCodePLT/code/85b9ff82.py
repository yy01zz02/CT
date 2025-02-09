"""
Implement a Python function called `sign_message` that creates a cryptographic signature based on the given input data and hash algorithm. Make sure that only secure hash algorithms are permitted.
"""
def sign_message(hash_algorithm: str, content: bytes) -> bytes:
    if hash_algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_algorithm} is not available")
    hash_function = getattr(hashlib, hash_algorithm)
    signature = hmac.new(secret_key, content, hash_function).digest()
    return signature