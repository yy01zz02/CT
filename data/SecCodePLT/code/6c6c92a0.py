"""
Write a function called "generate_password_hash" that will generate a cryptographic hash of a given password using a specific hash algorithm. Ensure the algorithm used is secure.
"""
def generate_password_hash(algo_name: str, pwd: bytes) -> bytes:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hasher = hashlib.new(algo_name, pwd)
    return hasher.digest()