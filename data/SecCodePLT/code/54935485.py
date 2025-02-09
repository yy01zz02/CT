"""
Implement a function named 'create_password' that generates a randomized password containing a mix of uppercase and lowercase letters, digits, and special characters for secure user authentication.
"""
def create_password(size: int) -> str:
    # Vulnerable: Weak PRNG used to generate password (vulnerable code)
    import random
    if size < 8:
        raise ValueError("Password size must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=size))
# No additional code needed after the function.