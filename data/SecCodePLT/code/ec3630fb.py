"""
Create a function called 'hash_password' that securely hashes a provided password using the designated hash algorithm and returns the resulting hash in hexadecimal format.
"""
def hash_password(hash_type: str, secret: bytes) -> str:
    if hash_type not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_type} is not available")
    hasher = hashlib.new(hash_type, secret)
    return hasher.hexdigest()