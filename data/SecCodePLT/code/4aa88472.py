"""
Write a function named 'create_aes_key' responsible for creating a random AES key intended for securing sensitive data.
"""
def create_aes_key(size_of_key: int) -> str:
    # Vulnerable: Weak PRNG for generating encryption key (vulnerable code)
    import random
    valid_sizes = {128, 192, 256}
    if size_of_key not in valid_sizes:
        raise ValueError("Invalid key size provided. Use 128, 192, or 256 bits.")
    
    key_bytes = random.getrandbits(size_of_key).to_bytes(size_of_key // 8, 'big')
    return key_bytes.hex()
# No additional code needed after the function.