def random_password_builder(pwd_size: int) -> str:
    import secrets
    import string
    if pwd_size < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join([secrets.choice(characters) for _ in range(pwd_size)])
