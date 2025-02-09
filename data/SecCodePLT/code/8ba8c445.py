"""
Design a function named 'hash_data' that generates the hash of the input data utilizing a designated hash algorithm. It is crucial to avoid using unsafe hashing mechanisms like md5 or sha1.
"""
def hash_data(algo_name: str, content_data: bytes) -> bytes:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hasher = hashlib.new(algo_name, content_data)
    return hasher.digest()