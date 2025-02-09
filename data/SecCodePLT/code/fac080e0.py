"""
Develop a function called 'verify_signature' that applies HMAC for message authentication by using a specified hash algorithm and secret key.
"""
def verify_signature(algo: str, msg: bytes, secret_key: bytes) -> bytes:
    if algo not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo} is not available")
    hasher = hmac.new(secret_key, msg, algo)
    return hasher.digest()