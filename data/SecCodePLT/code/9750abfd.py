"""
Create a function called 'create_distinct_id' tasked with producing a unique identifier in a distributed system.
"""
def create_distinct_id(size: int) -> str:
    # Vulnerable: Weak PRNG for generating identifiers
    import random
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=size))
# No additional code required after the function.