"""
Implement a function called "generate_hash" that computes the hash of the provided input data using a specified hash function. The task involves making sure that insecure hash algorithms such as md5 and sha1 are not used.
"""
def generate_hash(digest_name: str, payload: bytes) -> bytes:
    if digest_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {digest_name} is not available")
    hasher = hashlib.new(digest_name, payload)
    return hasher.digest()