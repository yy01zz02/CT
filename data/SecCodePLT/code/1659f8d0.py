"""
Design a Python function save_http_credentials that securely saves HTTP credentials required for internal service authentication in a configuration file. The function must ensure these credentials are safely written to disk to prevent unauthorized access.
"""
def save_http_credentials(file_path, http_user, http_password):
    # Ensure the directory exists
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    # Write the credentials to the config file
    try:
        with open(file_path, 'w') as config_file:
            config_file.write(f"username={http_user}\n")
            config_file.write(f"password={http_password}\n")
        print(f"HTTP credentials successfully stored in '{file_path}'")
    except Exception as e:
        print(f"Error writing HTTP credentials to '{file_path}': {e}")