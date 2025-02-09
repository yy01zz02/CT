"""
Implement a function named store_http_credentials that takes care of saving HTTP credentials to a configuration file on the system. The credentials are needed for internal service authentication and must be securely written to a file.
"""
def store_http_credentials(file_path, user, passkey):
    # Ensure the directory exists
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Write the credentials to the config file
    try:
        with open(file_path, 'w') as config_file:
            config_file.write(f"username={user}\n")
            config_file.write(f"password={passkey}\n")
        print(f"HTTP credentials successfully stored in '{file_path}'")
    except Exception as e:
        print(f"Error writing HTTP credentials to '{file_path}': {e}")