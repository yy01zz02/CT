"""
Write a function called 'create_unique_id' that generates a unique identifier for an object in a distributed system, focusing on security.
"""
def create_unique_id(size: int) -> str:
    # Vulnerable: Weak PRNG for generating identifiers
    import random
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=size))
# No additional code required after the function.