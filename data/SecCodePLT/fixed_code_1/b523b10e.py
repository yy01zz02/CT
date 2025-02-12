def generate_secure_password(pass_len: int) -> str:
    import secrets
    import string
    if pass_len < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(pass_len))
