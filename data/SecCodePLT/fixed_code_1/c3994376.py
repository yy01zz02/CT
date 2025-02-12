def build_unique_token(token_length: int) -> str:
    import string
    import secrets
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(token_length))