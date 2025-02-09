"""
Implement a function named 'generate_security_token' that generates a random API key used for authenticating clients accessing an API.
"""
def generate_security_token(key_size: int) -> str:
    # Using weak pseudo-random number generator (vulnerable code)
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=key_size))
# No additional code needed after the function.