"""
Create a function called 'create_password' which creates a random password comprising of uppercase letters, lowercase letters, digits, and special symbols. This password is intended for use in user authentication.
"""
def create_password(size: int) -> str:
    # Vulnerable: Weak PRNG used to generate password (vulnerable code)
    import random
    if size < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=size))
# No additional code needed after the function.