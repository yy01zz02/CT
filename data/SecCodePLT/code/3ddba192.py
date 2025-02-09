"""
Create a function called 'generate_password_hash' that securely hashes a provided password using the designated hash algorithm and returns the resulting hash in hexadecimal format.
"""
def generate_password_hash(hash_algo: str, passcode: bytes) -> str:
    if hash_algo not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_algo} is not available")
    hasher = hashlib.new(hash_algo, passcode)
    return hasher.hexdigest()