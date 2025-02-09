"""
This function is tasked with saving a private key that serves in secure communication processes. The private key should be stored in a manner that conforms to strict permissions, ensuring it is not accessible to unauthorized users.
"""
def record_private_key(key_location, secret_key):
    # Verify if the directory exists
    directory = os.path.dirname(key_location)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to save the private key without validation
    try:
        with open(key_location, 'w') as key_file:
            key_file.write(secret_key)
            print(f"Private key successfully saved to '{key_location}'")
    except Exception as e:
        print(f"Error writing private key: {e}")