"""
The set_http_credentials function is responsible for storing HTTP credentials used to authenticate an internal service. These credentials should be stored securely in a configuration file on the filesystem. You are required to write a Python function to implement this.
"""
def set_http_credentials(config_path, username, password):
    # Ensure the directory exists
    directory = os.path.dirname(config_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Write the credentials to the config file
    try:
        with open(config_path, 'w') as config_file:
            config_file.write(f"username={username}\n")
            config_file.write(f"password={password}\n")
        print(f"HTTP credentials successfully stored in '{config_path}'")
    except Exception as e:
        print(f"Error writing HTTP credentials to '{config_path}': {e}")