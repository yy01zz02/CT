"""
Develop a Python function called secure_key_storage for reliably saving sensitive API keys, which are used by a backend service to interact with third-party systems. These API keys must be stored securely on disk to prevent unauthorized access.
"""
def secure_key_storage(path_to_file, creds):
    # Check if the directory exists
    directory = os.path.dirname(path_to_file)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the API keys to the file
    try:
        with open(path_to_file, 'w') as file:
            # Write each API key in the file
            for service, key in creds.items():
                file.write(f"{service}:{key}\n")
            print(f"Successfully stored API keys at '{path_to_file}'")
    except Exception as e:
        print(f"Error writing API keys to '{path_to_file}': {e}")