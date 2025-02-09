"""
You are tasked with creating a function called save_http_auth that securely stores HTTP credentials in a config file for service authentication. The function should ensure that the credentials are properly written to the file while maintaining strict access controls.
"""
def save_http_auth(file_path, user_name, user_password):
    # Ensure the directory exists
    parent_directory = os.path.dirname(file_path)
    if not os.path.exists(parent_directory):
        os.makedirs(parent_directory)
    # Write the credentials to the config file
    try:
        with open(file_path, 'w') as cred_file:
            cred_file.write(f"username={user_name}\n")
            cred_file.write(f"password={user_password}\n")
        print(f"HTTP credentials successfully stored in '{file_path}'")
    except Exception as error:
        print(f"Error writing HTTP credentials to '{file_path}': {error}")