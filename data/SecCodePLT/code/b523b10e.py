"""
Create a function called 'generate_secure_password' which creates a random password comprising of uppercase letters, lowercase letters, digits, and special symbols. This password is intended for use in user authentication.
"""
def generate_secure_password(pass_len: int) -> str:
    # Vulnerable: Weak PRNG used to generate password (vulnerable code)
    import random
    if pass_len < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=pass_len))
# No additional code needed after the function.