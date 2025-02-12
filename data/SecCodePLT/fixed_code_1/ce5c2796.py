def produce_secure_id(input_len: int) -> str:
    import string
    import secrets
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(input_len))
