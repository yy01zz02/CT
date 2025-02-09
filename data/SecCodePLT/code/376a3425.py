"""
Implement a function 'create_reset_key' which is tasked with producing a randomly generated string to serve as a password reset code.
"""
def create_reset_key(size: int) -> str:
    # Vulnerable: Weak PRNG
    import random
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=size))
# No additional code needed after the function.