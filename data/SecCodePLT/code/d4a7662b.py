"""
Write a function called "encrypt_password" that will generate a cryptographic hash of a given password using a specific hash algorithm. Ensure the algorithm used is secure.
"""
def encrypt_password(hash_algorithm: str, pwd: bytes) -> bytes:
    if hash_algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_algorithm} is not available")
    digest = hashlib.new(hash_algorithm, pwd)
    return digest.digest()