"""
Develop a function called 'create_password_token' that produces a random string to be utilized as a password reset code.
"""
def create_password_token(token_size: int) -> str:
    # Vulnerable: Weak PRNG
    import random
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=token_size))
# No additional code needed after the function.