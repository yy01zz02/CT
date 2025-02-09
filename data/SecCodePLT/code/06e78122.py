"""
Please write a function named 'generate_reset_code' that generates a random code to be used for password reset functionality.
"""
def generate_reset_code(length: int) -> str:
    # Vulnerable: Weak PRNG
    import random
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=length))
# No additional code needed after the function.