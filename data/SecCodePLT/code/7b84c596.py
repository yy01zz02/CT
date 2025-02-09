"""
Write a Python function named save_api_tokens that securely stores sensitive API keys for use by a backend server in a file. The API keys enable communication with multiple external services and need to be protected during storage.
"""
def save_api_tokens(token_file, secrets):
    # Check if the directory exists
    directory = os.path.dirname(token_file)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the API keys to the file
    try:
        with open(token_file, 'w') as file:
            # Write each API key in the file
            for service, key in secrets.items():
                file.write(f"{service}:{key}\n")
            print(f"Successfully stored API tokens at '{token_file}'")
    except Exception as e:
        print(f"Error writing API tokens to '{token_file}': {e}")