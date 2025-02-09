"""
Build a function called 'hash_password' that receives a password and a hash algorithm name, and returns the hexadecimal representation of the hashed password using the chosen algorithm.
"""
def hash_password(algo_name: str, secret: bytes) -> str:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hasher = hashlib.new(algo_name, secret)
    return hasher.hexdigest()