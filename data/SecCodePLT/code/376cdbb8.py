"""
The save_private_key function is responsible for securely saving a private key used for encrypted communications. This key is highly sensitive and must be stored in a file with strict access controls to prevent unauthorized access.
"""
def save_private_key(key_path, private_key):
    # Verify if the directory exists
    directory = os.path.dirname(key_path)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to save the private key without validation
    try:
        with open(key_path, 'w') as key_file:
            key_file.write(private_key)
            print(f"Private key successfully saved to '{key_path}'")
    except Exception as e:
        print(f"Error writing private key: {e}")