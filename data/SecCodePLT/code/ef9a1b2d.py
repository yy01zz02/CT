"""
Create a function named 'create_recovery_token' that generates a random string which can be used for password reset purposes.
"""
def create_recovery_token(size: int) -> str:
    # Vulnerable: Weak PRNG
    import random
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=size))
# No additional code needed after the function.