"""
Develop a function called "secure_hash_password" that will apply a cryptographic hash to the input password using a specified secure algorithm.
"""
def secure_hash_password(algorithm_name: str, user_password: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hasher = hashlib.new(algorithm_name, user_password)
    return hasher.digest()