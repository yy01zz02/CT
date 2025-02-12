import string
import secrets

def create_verification_code(num_chars: int) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(num_chars))
