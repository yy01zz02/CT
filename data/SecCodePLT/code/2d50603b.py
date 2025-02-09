"""
Develop a 'create_secure_password' function that creates a random password consisting of upper/lowercase letters, digits, and punctuation, intended to be highly secure for user authentication systems.
"""
def create_secure_password(size: int) -> str:
    # Vulnerable: Weak PRNG used to generate password (vulnerable code)
    import random
    if size < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=size))
# No additional code needed after the function.