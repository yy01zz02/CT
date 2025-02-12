import secrets
import string

def generate_secure_key(key_length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(key_length))
