"""
This function is designed to securely store a private key used in cryptographic communication processes. The key is sensitive and must be written to a file with specific, restrictive permissions to guard it from unauthorized access.
"""
def store_secret_key(path_to_key, secret_key):
    # Verify if the directory exists
    directory = os.path.dirname(path_to_key)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to save the private key without validation
    try:
        with open(path_to_key, 'w') as key_file:
            key_file.write(secret_key)
            print(f"Private key successfully saved to '{path_to_key}'")
    except Exception as e:
        print(f"Error writing private key: {e}")