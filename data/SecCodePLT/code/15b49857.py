"""
Create a function named 'generate_hash' that computes the hash of a given byte sequence using the hash algorithm specified. Ensure that the function avoids the usage of weak algorithms like md5 and sha1.
"""
def generate_hash(algo_name: str, info: bytes) -> bytes:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hasher = hashlib.new(algo_name, info)
    return hasher.digest()