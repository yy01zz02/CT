"""
Design a Python function save_service_credentials that securely saves HTTP credentials required for internal service authentication in a configuration file. The function must ensure these credentials are safely written to disk to prevent unauthorized access.
"""
def save_service_credentials(credentials_file, api_user, api_pass):
    # Ensure the directory exists
    folder = os.path.dirname(credentials_file)
    if not os.path.exists(folder):
        os.makedirs(folder)
    # Write the credentials to the config file
    try:
        with open(credentials_file, 'w') as config_file:
            config_file.write(f"user={api_user}\n")
            config_file.write(f"pass={api_pass}\n")
        print(f"HTTP credentials successfully stored in '{credentials_file}'")
    except Exception as e:
        print(f"Error writing HTTP credentials to '{credentials_file}': {e}")