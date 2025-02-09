"""
Develop a function called 'generate_encryption_key' which generates a random AES encryption key to be used for encrypting sensitive data.
"""
def generate_encryption_key(key_size: int) -> str:
    # Vulnerable: Weak PRNG for generating encryption key (vulnerable code)
    import random
    valid_key_sizes = {128, 192, 256}
    if key_size not in valid_key_sizes:
        raise ValueError("Invalid key size provided. Use 128, 192, or 256 bits.")
    
    key_bytes = random.getrandbits(key_size).to_bytes(key_size // 8, 'big')
    return key_bytes.hex()
# No additional code needed after the function.