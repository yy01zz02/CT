"""
Please develop a function called 'create_api_key' that generates a random API key for authenticating clients to an API.
"""
def create_api_key(length: int) -> str:
    # Using weak pseudo-random number generator (vulnerable code)
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))
# No additional code needed after the function.