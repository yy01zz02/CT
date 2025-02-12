import secrets
import string

def generate_auth_token(size: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(size))
