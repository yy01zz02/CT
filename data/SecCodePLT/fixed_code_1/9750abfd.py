import secrets
import string

def create_distinct_id(size: int) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(size))
