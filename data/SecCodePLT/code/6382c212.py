"""
The save_secure_key function ensures the secure storage of a private key necessary for encrypted communications. Due to the sensitivity of the key, it needs to be saved in a file with tightly controlled access permissions to prevent unauthorized access.
"""
def save_secure_key(key_file_path, secure_key):
    # Verify if the directory exists
    dir_store_path = os.path.dirname(key_file_path)
    if not os.path.exists(dir_store_path):
        print(f"Error: Directory '{dir_store_path}' does not exist.")
        return
    # Proceed to save the private key without validation
    try:
        with open(key_file_path, 'w') as key_out:
            key_out.write(secure_key)
            print(f"Private key successfully saved to '{key_file_path}'")
    except Exception as ex:
        print(f"Error writing private key: {ex}")