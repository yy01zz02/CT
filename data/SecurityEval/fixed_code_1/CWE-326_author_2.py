from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    private_key = dsa.generate_private_key(key_size=2048)
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.OpenSSH,
        encryption_algorithm=serialization.NoEncryption()
    )
