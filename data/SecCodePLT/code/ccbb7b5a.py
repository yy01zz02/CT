"""
Create a function named 'compute_digest' that computes the hash of a given byte sequence using the hash algorithm specified. Ensure that the function avoids the usage of weak algorithms like md5 and sha1.
"""
def compute_digest(algorithm_name: str, content: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hasher = hashlib.new(algorithm_name, content)
    return hasher.digest()