def generate_secure_token(token_size: int) -> str:
    import secrets
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(token_size))
