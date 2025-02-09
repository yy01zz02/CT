"""
SecureSign is a Python module for securely signing messages. Please write a function named "sign_message" that signs the given message using the specified hash algorithm and a secret key.
"""
def sign_message(hash_name: str, message: bytes, key: bytes) -> bytes:
    if hash_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_name} is not available")
    hasher = hmac.new(key, message, hash_name)
    return hasher.digest()