import string
import secrets

def generate_access_token(api_length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(api_length))
