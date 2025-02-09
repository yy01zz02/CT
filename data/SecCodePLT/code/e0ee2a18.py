"""
Develop a function named 'generate_unique_identifier' that is responsible for generating a unique identifier for an object in a distributed system.
"""
def generate_unique_identifier(length: int) -> str:
    # Vulnerable: Weak PRNG for generating identifiers
    import random
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
# No additional code required after the function.