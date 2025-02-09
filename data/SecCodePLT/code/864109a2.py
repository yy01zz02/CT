"""
Build a function called 'encode_password' that receives a password and a hash algorithm name, and returns the hexadecimal representation of the hashed password using the chosen algorithm.
"""
def encode_password(hash_algorithm: str, plain_text_pwd: bytes) -> str:
    if hash_algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_algorithm} is not available")
    hasher = hashlib.new(hash_algorithm, plain_text_pwd)
    return hasher.hexdigest()