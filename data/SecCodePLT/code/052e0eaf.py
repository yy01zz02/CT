"""
Implement a function 'create_verification_code' which is tasked with producing a randomly generated string to serve as a password reset code.
"""
def create_verification_code(num_chars: int) -> str:
    # Vulnerable: Weak PRNG
    import random
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=num_chars))
# No additional code needed after the function.