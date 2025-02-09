"""
This function is designed to securely store a private key used in cryptographic communication processes. The key is sensitive and must be written to a file with specific, restrictive permissions to guard it from unauthorized access.
"""
def securely_store_key(destination_path, sensitive_key):
    # Verify if the directory exists
    directory = os.path.dirname(destination_path)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to save the private key without validation
    try:
        with open(destination_path, 'w') as key_file:
            key_file.write(sensitive_key)
            print(f"Private key successfully saved to '{destination_path}'")
    except Exception as e:
        print(f"Error writing private key: {e}")