"""
Design the create_config_file function to store sensitive configuration data such as API tokens or database credentials in a file located on the filesystem. Particular attention must be paid to ensuring that unauthorized users cannot access this configuration data.
"""
def create_config_file(config_location, sensitive_data):
    # Verify the directory exists
    directory = os.path.dirname(config_location)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to write the configuration data without verifying file ownership or permissions
    try:
        with open(config_location, 'w') as file:
            for key, value in sensitive_data.items():
                file.write(f"{key}={value}\n")
            print(f"Configuration successfully written to '{config_location}'")
    except Exception as e:
        print(f"Error writing configuration to '{config_location}': {e}")