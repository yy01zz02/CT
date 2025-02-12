def produce_unique_key(key_length: int) -> str:
    import secrets
    import string
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(key_length))