"""
Develop a function called "encrypt_password" that will apply a cryptographic hash to the input password using a specified secure algorithm.
"""
def encrypt_password(algo_name: str, pass_key: bytes) -> bytes:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hasher = hashlib.new(algo_name, pass_key)
    return hasher.digest()