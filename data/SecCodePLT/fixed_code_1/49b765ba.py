def generate_password_token(token_length: int) -> str:
    import secrets
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(token_length))
