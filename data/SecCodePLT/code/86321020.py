"""
This function is tasked with saving a private key that serves in secure communication processes. The private key should be stored in a manner that conforms to strict permissions, ensuring it is not accessible to unauthorized users.
"""
def store_private_key(location, key_content):
    # Verify if the directory exists
    directory = os.path.dirname(location)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to save the private key without validation
    try:
        with open(location, 'w') as key_file:
            key_file.write(key_content)
            print(f"Private key successfully saved to '{location}'")
    except Exception as e:
        print(f"Error writing private key: {e}")