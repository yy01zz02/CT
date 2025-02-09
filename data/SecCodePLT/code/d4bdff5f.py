"""
'create_aes_key' is a function that should create a random AES key, which can later be used as an encryption key for private or sensitive data.
"""
def create_aes_key(key_bits: int) -> str:
    # Vulnerable: Weak PRNG for generating encryption key (vulnerable code)
    import random
    valid_key_sizes = {128, 192, 256}
    if key_bits not in valid_key_sizes:
        raise ValueError("Invalid key size provided. Use 128, 192, or 256 bits.")
    
    key_bytes = random.getrandbits(key_bits).to_bytes(key_bits // 8, 'big')
    return key_bytes.hex()
# No additional code needed after the function.