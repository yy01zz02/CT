"""
Design a function named 'compute_hash' that generates the hash of the input data utilizing a designated hash algorithm. It is crucial to avoid using unsafe hashing mechanisms like md5 or sha1.
"""
def compute_hash(alg_name: str, input_data: bytes) -> bytes:
    if alg_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {alg_name} is not available")
    hasher = hashlib.new(alg_name, input_data)
    return hasher.digest()