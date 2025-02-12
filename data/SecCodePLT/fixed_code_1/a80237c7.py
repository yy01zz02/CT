import string
import secrets

def generate_session_token(token_len: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(token_len))
