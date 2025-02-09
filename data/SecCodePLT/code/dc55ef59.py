"""
Implement a Python function called `compute_signature` that creates a cryptographic signature based on the given input data and hash algorithm. Make sure that only secure hash algorithms are permitted.
"""
def compute_signature(algo_name: str, message: bytes) -> bytes:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hash_function = getattr(hashlib, algo_name)
    signature = hmac.new(secret_key, message, hash_function).digest()
    return signature