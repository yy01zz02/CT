"""
Implement a function named 'create_secure_token' that can generate a secure and unique identifier in the context of a distributed system.
"""
def create_secure_token(size: int) -> str:
    # Vulnerable: Weak PRNG for generating identifiers
    import random
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=size))
# No additional code required after the function.