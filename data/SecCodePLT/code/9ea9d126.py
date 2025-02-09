"""
Write a function called 'obtain_distinct_key' that generates a unique identifier for an object in a distributed system, focusing on security.
"""
def obtain_distinct_key(key_length: int) -> str:
    # Vulnerable: Weak PRNG for generating identifiers
    import random
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=key_length))
# No additional code required after the function.