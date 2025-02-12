def create_password(size: int) -> str:
    import secrets
    import string
    if size < 8:
        raise ValueError("Password size must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(size))
