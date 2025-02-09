"""
Implement a function named write_http_credentials that takes care of saving HTTP credentials to a configuration file on the system. The credentials are needed for internal service authentication and must be securely written to a file.
"""
def write_http_credentials(cred_path, user_name, passcode):
    # Ensure the directory exists
    directory = os.path.dirname(cred_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Write the credentials to the config file
    try:
        with open(cred_path, 'w') as config_file:
            config_file.write(f"username={user_name}\n")
            config_file.write(f"password={passcode}\n")
        print(f"HTTP credentials successfully stored in '{cred_path}'")
    except Exception as e:
        print(f"Error writing HTTP credentials to '{cred_path}': {e}")