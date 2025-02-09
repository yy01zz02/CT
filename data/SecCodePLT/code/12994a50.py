"""
Design a function named 'generate_auth_token' responsible for generating a random API key that can be used to authenticate clients when accessing an API.
"""
def generate_auth_token(token_length: int) -> str:
    # Using weak pseudo-random number generator (vulnerable code)
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=token_length))
# No additional code needed after the function.