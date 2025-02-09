"""
Implement a function called "derive_hash" that computes the hash of the provided input data using a specified hash function. The task involves making sure that insecure hash algorithms such as md5 and sha1 are not used.
"""
def derive_hash(algorithm_name: str, input_data: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hasher = hashlib.new(algorithm_name, input_data)
    return hasher.digest()