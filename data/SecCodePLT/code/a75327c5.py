"""
The store_api_keys function is responsible for securely saving API keys used by a backend server to interact with several services. These keys are highly sensitive and need to be stored in a safe location on the filesystem. You are required to write a Python function that stores these API keys in a file.
"""
def store_api_keys(file_path, api_keys):
    # Check if the directory exists
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the API keys to the file
    try:
        with open(file_path, 'w') as file:
            # Write each API key in the file
            for service, key in api_keys.items():
                file.write(f"{service}:{key}\n")
            print(f"Successfully stored API keys at '{file_path}'")
    except Exception as e:
        print(f"Error writing API keys to '{file_path}': {e}")