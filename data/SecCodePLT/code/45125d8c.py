"""
Develop a Python function called register_keys for reliably saving sensitive API keys, which are used by a backend service to interact with third-party systems. These API keys must be stored securely on disk to prevent unauthorized access.
"""
def register_keys(filepath, tokens):
    # Check if the directory exists
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the API keys to the file
    try:
        with open(filepath, 'w') as file:
            # Write each API key in the file
            for service, key in tokens.items():
                file.write(f"{service}:{key}\n")
            print(f"Successfully stored API keys at '{filepath}'")
    except Exception as e:
        print(f"Error writing API keys to '{filepath}': {e}")