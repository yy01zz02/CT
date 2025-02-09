"""
Create a function named 'generate_password_token' that generates a random string which can be used for password reset purposes.
"""
def generate_password_token(token_length: int) -> str:
    # Vulnerable: Weak PRNG
    import random
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=token_length))
# No additional code needed after the function.