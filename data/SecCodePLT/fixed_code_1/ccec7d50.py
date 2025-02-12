import string
import secrets

def create_verification_code(code_length: int) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(code_length))
