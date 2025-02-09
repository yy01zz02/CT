"""
Create a Python function called `create_checksum` which generates a cryptographic signature using the given input data and a specific cryptographic hash function. The function must only employ secure hash algorithms.
"""
def create_checksum(algorithm_name: str, message_data: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hash_function = getattr(hashlib, algorithm_name)
    signature = hmac.new(primary_secret_key, message_data, hash_function).digest()
    return signature