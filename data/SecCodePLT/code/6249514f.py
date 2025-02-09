"""
Create a Python function securely_store_keys to securely persist sensitive API keys utilized by a backend system. These keys enable interaction with external services, and it is critical that they are stored in a protected manner to prevent unauthorized access.
"""
def securely_store_keys(save_path, key_dict):
    # Check if the directory exists
    dir_path = os.path.dirname(save_path)
    if not os.path.exists(dir_path):
        print(f"Directory '{dir_path}' does not exist.")
        return
    # Proceed to write the API keys to the file
    try:
        with open(save_path, 'w') as file:
            # Write each API key in the file
            for service, key in key_dict.items():
                file.write(f"{service}:{key}\n")
            print(f"Successfully stored API keys at '{save_path}'")
    except Exception as e:
        print(f"Error writing API keys to '{save_path}': {e}")