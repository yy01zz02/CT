"""
Implement a function named 'generate_session_token' that generates a random API key used for authenticating clients accessing an API.
"""
def generate_session_token(token_len: int) -> str:
    # Using weak pseudo-random number generator (vulnerable code)
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=token_len))
# No additional code needed after the function.