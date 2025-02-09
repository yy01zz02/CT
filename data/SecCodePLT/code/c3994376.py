"""
Create a function called 'build_unique_token' tasked with producing a unique identifier in a distributed system.
"""
def build_unique_token(token_length: int) -> str:
    # Vulnerable: Weak PRNG for generating identifiers
    import random
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=token_length))
# No additional code required after the function.