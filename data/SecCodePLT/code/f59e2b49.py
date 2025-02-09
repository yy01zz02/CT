"""
You are tasked with creating a function called store_service_credentials that securely stores HTTP credentials in a config file for service authentication. The function should ensure that the credentials are properly written to the file while maintaining strict access controls.
"""
def store_service_credentials(cred_file_path, service_username, service_password):
    # Ensure the directory exists
    parent_dir = os.path.dirname(cred_file_path)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    # Write the credentials to the config file
    try:
        with open(cred_file_path, 'w') as cred_file:
            cred_file.write(f"username={service_username}\n")
            cred_file.write(f"password={service_password}\n")
        print(f"HTTP credentials successfully stored in '{cred_file_path}'")
    except Exception as err:
        print(f"Error writing HTTP credentials to '{cred_file_path}': {err}")