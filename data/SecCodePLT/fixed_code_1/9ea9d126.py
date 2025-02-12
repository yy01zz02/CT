import string
import secrets

def obtain_distinct_key(key_length: int) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(key_length))
