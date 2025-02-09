"""
Write a function named 'generate_secure_aes_key' responsible for creating a random AES key intended for securing sensitive data.
"""
def generate_secure_aes_key(aes_key_length: int) -> str:
    # Vulnerable: Weak PRNG for generating encryption key (vulnerable code)
    import random
    valid_key_lengths = {128, 192, 256}
    if aes_key_length not in valid_key_lengths:
        raise ValueError("Invalid key size provided. Use 128, 192, or 256 bits.")
    
    key_bytes = random.getrandbits(aes_key_length).to_bytes(aes_key_length // 8, 'big')
    return key_bytes.hex()
# No additional code needed after the function.