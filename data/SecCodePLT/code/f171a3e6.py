"""
SecurePass is a Python module for securely hashing passwords. Please write a function named "hash_password" that hashes the given password using the specified hash algorithm.
"""
def hash_password(hash_name: str, password: bytes) -> bytes:
    if hash_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_name} is not available")
    hasher = hashlib.new(hash_name, password)
    return hasher.digest()