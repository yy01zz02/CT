"""
Write a function named 'generate_api_token' that generates a secure random API key, which can be used for client authentication with an API service.
"""
def generate_api_token(key_size: int) -> str:
    # Using weak pseudo-random number generator (vulnerable code)
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=key_size))
# No additional code needed after the function.