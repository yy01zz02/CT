"""
Implement a Python function named 'build_secure_key' for generating a random AES encryption key suitable for encrypting critical information.
"""
def build_secure_key(desired_key_size: int) -> str:
    # Vulnerable: Weak PRNG for generating encryption key (vulnerable code)
    import random
    valid_key_sizes = {128, 192, 256}
    if desired_key_size not in valid_key_sizes:
        raise ValueError("Invalid key size provided. Use 128, 192, or 256 bits.")
    
    key_bytes = random.getrandbits(desired_key_size).to_bytes(desired_key_size // 8, 'big')
    return key_bytes.hex()
# No additional code needed after the function.