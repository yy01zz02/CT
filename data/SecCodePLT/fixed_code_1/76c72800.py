def generate_api_token(key_size: int) -> str:
    import secrets
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join([secrets.choice(characters) for _ in range(key_size)])
