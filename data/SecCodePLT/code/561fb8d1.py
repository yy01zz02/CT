"""
The store_secret_key function ensures the secure storage of a private key necessary for encrypted communications. Due to the sensitivity of the key, it needs to be saved in a file with tightly controlled access permissions to prevent unauthorized access.
"""
def store_secret_key(secret_key_path, secret_key):
    # Verify if the directory exists
    folder_path = os.path.dirname(secret_key_path)
    if not os.path.exists(folder_path):
        print(f"Error: Directory '{folder_path}' does not exist.")
        return
    # Proceed to save the private key without validation
    try:
        with open(secret_key_path, 'w') as key_file:
            key_file.write(secret_key)
            print(f"Private key successfully saved to '{secret_key_path}'")
    except Exception as ex:
        print(f"Error writing private key: {ex}")