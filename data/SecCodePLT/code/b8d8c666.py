"""
Implement a Python function called `create_signature` that creates a cryptographic signature based on the given input data and hash algorithm. Make sure that only secure hash algorithms are permitted.
"""
def create_signature(algorithm_name: str, payload: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hash_function = getattr(hashlib, algorithm_name)
    signature = hmac.new(secret_key, payload, hash_function).digest()
    return signature