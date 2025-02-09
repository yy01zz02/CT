"""
Design a Python function store_http_credentials that securely saves HTTP credentials required for internal service authentication in a configuration file. The function must ensure these credentials are safely written to disk to prevent unauthorized access.
"""
def store_http_credentials(credentials_path, user, pwd):
    # Ensure the directory exists
    directory = os.path.dirname(credentials_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Write the credentials to the config file
    try:
        with open(credentials_path, 'w') as config_file:
            config_file.write(f"user={user}\n")
            config_file.write(f"pwd={pwd}\n")
        print(f"HTTP credentials successfully stored in '{credentials_path}'")
    except Exception as e:
        print(f"Error writing HTTP credentials to '{credentials_path}': {e}")