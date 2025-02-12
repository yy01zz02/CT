def build_secure_token(length_of_token: int) -> str:
    import secrets
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length_of_token))
