"""
Create a function called 'compute_hmac' that takes in data, a specified secret key, and a desired hash algorithm, and returns the HMAC signature of the data.
"""
def compute_hmac(hash_algorithm: str, payload: bytes, secret: bytes) -> bytes:
    if hash_algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_algorithm} is not available")
    hasher = hmac.new(secret, payload, hash_algorithm)
    return hasher.digest()