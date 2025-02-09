from cryptography.fernet import Fernet

def send_encrypted(secret_key, channel, message):
    cipher = Fernet(secret_key)
    encrypted = cipher.encrypt(message)
    channel.send(encrypted)