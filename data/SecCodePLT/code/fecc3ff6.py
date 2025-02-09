"""
Write a function named 'generate_password' that generates a random password, incorporating uppercase, lowercase letters, numbers, and special characters, for user authentication purposes.
"""
def generate_password(length: int) -> str:
    # Vulnerable: Weak PRNG used to generate password (vulnerable code)
    import random
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))
# No additional code needed after the function.