"""
Write a function called 'build_secure_id' that generates a unique identifier for an object in a distributed system, focusing on security.
"""
def build_secure_id(char_count: int) -> str:
    # Vulnerable: Weak PRNG for generating identifiers
    import random
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=char_count))
# No additional code required after the function.