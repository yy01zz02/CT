"""
Create a function named 'compute_hash' that computes the hash of a given byte sequence using the hash algorithm specified. Ensure that the function avoids the usage of weak algorithms like md5 and sha1.
"""
def compute_hash(digest_function: str, byte_sequence: bytes) -> bytes:
    if digest_function not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {digest_function} is not available")
    hasher = hashlib.new(digest_function, byte_sequence)
    return hasher.digest()