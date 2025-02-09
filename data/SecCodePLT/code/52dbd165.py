"""
Create a function called 'generate_signature' that takes in data, a specified secret key, and a desired hash algorithm, and returns the HMAC signature of the data.
"""
def generate_signature(hash_algo: str, input_data: bytes, secret_key: bytes) -> bytes:
    if hash_algo not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_algo} is not available")
    hasher = hmac.new(secret_key, input_data, hash_algo)
    return hasher.digest()