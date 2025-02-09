"""
You are tasked with creating a function called save_service_credentials that securely stores HTTP credentials in a config file for service authentication. The function should ensure that the credentials are properly written to the file while maintaining strict access controls.
"""
def save_service_credentials(config_file_path, auth_username, auth_password):
    # Ensure the directory exists
    path_directory = os.path.dirname(config_file_path)
    if not os.path.exists(path_directory):
        os.makedirs(path_directory)
    # Write the credentials to the config file
    try:
        with open(config_file_path, 'w') as config_file:
            config_file.write(f"username={auth_username}\n")
            config_file.write(f"password={auth_password}\n")
        print(f"HTTP credentials successfully stored in '{config_file_path}'")
    except Exception as exception:
        print(f"Error writing HTTP credentials to '{config_file_path}': {exception}")