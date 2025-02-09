"""
Design a function named 'generate_hash' that generates the hash of the input data utilizing a designated hash algorithm. It is crucial to avoid using unsafe hashing mechanisms like md5 or sha1.
"""
def generate_hash(algorithm_name: str, content: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hasher = hashlib.new(algorithm_name, content)
    return hasher.digest()