"""
Create a function named 'create_verification_code' that generates a random string which can be used for password reset purposes.
"""
def create_verification_code(code_length: int) -> str:
    # Vulnerable: Weak PRNG
    import random
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=code_length))
# No additional code needed after the function.