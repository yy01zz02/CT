"""
Write a Python function named archive_secret_tokens that securely stores sensitive API keys for use by a backend server in a file. The API keys enable communication with multiple external services and need to be protected during storage.
"""
def archive_secret_tokens(store_file, token_data):
    # Check if the directory exists
    dir_name = os.path.dirname(store_file)
    if not os.path.exists(dir_name):
        print(f"Directory '{dir_name}' does not exist.")
        return
    # Proceed to write the API keys to the file
    try:
        with open(store_file, 'w') as file:
            # Write each API key in the file
            for svc_name, api_key in token_data.items():
                file.write(f"{svc_name}:{api_key}\n")
            print(f"Successfully stored API keys at '{store_file}'")
    except Exception as e:
        print(f"Error writing API keys to '{store_file}': {e}")