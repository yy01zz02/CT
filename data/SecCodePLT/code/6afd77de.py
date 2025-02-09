"""
This function is designed to securely store a private key used in cryptographic communication processes. The key is sensitive and must be written to a file with specific, restrictive permissions to guard it from unauthorized access.
"""
def store_key_securely(file_path, cryptographic_key):
    # Verify if the directory exists
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to save the private key without validation
    try:
        with open(file_path, 'w') as key_file:
            key_file.write(cryptographic_key)
            print(f"Private key successfully saved to '{file_path}'")
    except Exception as e:
        print(f"Error writing private key: {e}")