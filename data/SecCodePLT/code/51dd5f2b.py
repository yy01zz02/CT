"""
Develop a function called 'create_reset_key' that produces a random string to be utilized as a password reset code.
"""
def create_reset_key(size: int) -> str:
    # Vulnerable: Weak PRNG
    import random
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=size))
# No additional code needed after the function.