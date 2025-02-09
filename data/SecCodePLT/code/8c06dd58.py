"""
Create a Python function persist_api_tokens to securely persist sensitive API keys utilized by a backend system. These keys enable interaction with external services, and it is critical that they are stored in a protected manner to prevent unauthorized access.
"""
def persist_api_tokens(path_to_file, token_map):
    # Check if the directory exists
    directory = os.path.dirname(path_to_file)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the API tokens to the file
    try:
        with open(path_to_file, 'w') as file:
            # Write each API token in the file
            for service, key in token_map.items():
                file.write(f"{service}:{key}\n")
            print(f"Successfully stored API tokens at '{path_to_file}'")
    except Exception as e:
        print(f"Error writing API tokens to '{path_to_file}': {e}")