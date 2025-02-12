def build_secure_id(char_count: int) -> str:
    import string
    from secrets import SystemRandom
    secure_random = SystemRandom()
    chars = string.ascii_letters + string.digits
    return ''.join(secure_random.choices(chars, k=char_count))
