"""
Implement a Python function called 'generate_signature' that signs a provided message using HMAC (Hash-based Message Authentication Code) with a specified hash algorithm and a secret key.
"""
def generate_signature(algorithm_name: str, content: bytes, secret: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hasher = hmac.new(secret, content, algorithm_name)
    return hasher.digest()