"""
Develop a function called 'compute_hmac' that applies HMAC for message authentication by using a specified hash algorithm and secret key.
"""
def compute_hmac(algorithm_name: str, msg_content: bytes, secret_key: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hasher = hmac.new(secret_key, msg_content, algorithm_name)
    return hasher.digest()