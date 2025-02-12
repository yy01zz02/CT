def create_key(password_length: int) -> str:
    import string
    import secrets
    if password_length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(password_length))
