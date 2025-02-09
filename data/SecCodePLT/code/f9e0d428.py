"""
Write a Python function named securely_save_api_keys that securely stores sensitive API keys for use by a backend server in a file. The API keys enable communication with multiple external services and need to be protected during storage.
"""
def securely_save_api_keys(path_to_file, key_data):
    # Check if the directory exists
    directory_path = os.path.dirname(path_to_file)
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return
    # Proceed to write the API keys to the file
    try:
        with open(path_to_file, 'w') as file:
            # Write each API key in the file
            for svc, secret in key_data.items():
                file.write(f"{svc}:{secret}\n")
            print(f"Successfully stored API keys at '{path_to_file}'")
    except Exception as e:
        print(f"Error writing API keys to '{path_to_file}': {e}")