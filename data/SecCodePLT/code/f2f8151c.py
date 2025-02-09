"""
Create a Python function save_credentials to securely persist sensitive API keys utilized by a backend system. These keys enable interaction with external services, and it is critical that they are stored in a protected manner to prevent unauthorized access.
"""
def save_credentials(destination_path, credentials_dict):
    # Check if the directory exists
    directory = os.path.dirname(destination_path)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the API keys to the file
    try:
        with open(destination_path, 'w') as file:
            # Write each API key in the file
            for service, key in credentials_dict.items():
                file.write(f"{service}:{key}\n")
            print(f"Successfully stored API keys at '{destination_path}'")
    except Exception as e:
        print(f"Error writing API keys to '{destination_path}': {e}")