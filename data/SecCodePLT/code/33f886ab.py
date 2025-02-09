"""
'generate_secure_key' is a function that should create a random AES key, which can later be used as an encryption key for private or sensitive data.
"""
def generate_secure_key(bits: int) -> str:
    # Vulnerable: Weak PRNG for generating encryption key (vulnerable code)
    import random
    acceptable_bits = {128, 192, 256}
    if bits not in acceptable_bits:
        raise ValueError("Invalid key size provided. Use 128, 192, or 256 bits.")
    
    bytes_key = random.getrandbits(bits).to_bytes(bits // 8, 'big')
    return bytes_key.hex()
# No additional code needed after the function.