def generate_security_token(key_size: int) -> str:
    import string
    import secrets
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(key_size))
