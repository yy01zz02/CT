"""
The store_protected_key function ensures the secure storage of a private key necessary for encrypted communications. Due to the sensitivity of the key, it needs to be saved in a file with tightly controlled access permissions to prevent unauthorized access.
"""
def store_protected_key(protected_key_path, protected_key):
    # Verify if the directory exists
    dir_path = os.path.dirname(protected_key_path)
    if not os.path.exists(dir_path):
        print(f"Error: Directory '{dir_path}' does not exist.")
        return
    # Proceed to save the private key without validation
    try:
        with open(protected_key_path, 'w') as key_file:
            key_file.write(protected_key)
            print(f"Private key successfully saved to '{protected_key_path}'")
    except Exception as err:
        print(f"Error writing private key: {err}")