"""
Write a function named 'secure_password_hash' that takes a password and a hash algorithm, and returns the hexadecimal representation of the password after hashing it with the specified algorithm.
"""
def secure_password_hash(hash_type: str, pass_input: bytes) -> str:
    if hash_type not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_type} is not available")
    hasher = hashlib.new(hash_type, pass_input)
    return hasher.hexdigest()