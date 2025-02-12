import string
import secrets

def generate_auth_token(token_length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(token_length))
