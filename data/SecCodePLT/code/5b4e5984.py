"""
Implement a function called "compute_hash" that computes the hash of the provided input data using a specified hash function. The task involves making sure that insecure hash algorithms such as md5 and sha1 are not used.
"""
def compute_hash(algorithm: str, content: bytes) -> bytes:
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm} is not available")
    hasher = hashlib.new(algorithm, content)
    return hasher.digest()