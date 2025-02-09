"""
Build a function called 'encrypt_pwd' that receives a password and a hash algorithm name, and returns the hexadecimal representation of the hashed password using the chosen algorithm.
"""
def encrypt_pwd(hash_algo: str, pwd: bytes) -> str:
    if hash_algo not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_algo} is not available")
    hasher = hashlib.new(hash_algo, pwd)
    return hasher.hexdigest()