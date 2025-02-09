"""
Develop a function called 'generate_temp_key' that produces a random string to be utilized as a password reset code.
"""
def generate_temp_key(size_of_key: int) -> str:
    # Vulnerable: Weak PRNG
    import random
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=size_of_key))
# No additional code needed after the function.