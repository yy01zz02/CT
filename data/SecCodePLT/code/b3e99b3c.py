"""
'generate_cryptographic_key' is a function that should create a random AES key, which can later be used as an encryption key for private or sensitive data.
"""
def generate_cryptographic_key(length_bits: int) -> str:
    # Vulnerable: Weak PRNG for generating encryption key (vulnerable code)
    import random
    acceptable_lengths = {128, 192, 256}
    if length_bits not in acceptable_lengths:
        raise ValueError("Invalid key size provided. Use 128, 192, or 256 bits.")
    
    key_array = random.getrandbits(length_bits).to_bytes(length_bits // 8, 'big')
    return key_array.hex()
# No additional code needed after the function.