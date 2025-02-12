import string
import secrets

def make_password(pw_length: int) -> str:
    if pw_length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(pw_length))