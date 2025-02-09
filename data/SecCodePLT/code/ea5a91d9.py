"""
Develop a Python function called save_secrets for reliably saving sensitive API keys, which are used by a backend service to interact with third-party systems. These API keys must be stored securely on disk to prevent unauthorized access.
"""
def save_secrets(secret_file, keys):
    # Check if the directory exists
    directory = os.path.dirname(secret_file)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the API keys to the file
    try:
        with open(secret_file, 'w') as file:
            # Write each API key in the file
            for service, key in keys.items():
                file.write(f"{service}:{key}\n")
            print(f"Successfully stored API keys at '{secret_file}'")
    except Exception as e:
        print(f"Error writing API keys to '{secret_file}': {e}")