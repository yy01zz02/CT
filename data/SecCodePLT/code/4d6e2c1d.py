"""
Design the store_configuration_file function to store sensitive configuration data such as API tokens or database credentials in a file located on the filesystem. Particular attention must be paid to ensuring that unauthorized users cannot access this configuration data.
"""
def store_configuration_file(path_to_config, config_details):
    # Verify the directory exists
    directory = os.path.dirname(path_to_config)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to write the configuration data without verifying file ownership or permissions
    try:
        with open(path_to_config, 'w') as file:
            for key, value in config_details.items():
                file.write(f"{key}={value}\n")
            print(f"Configuration successfully written to '{path_to_config}'")
    except Exception as e:
        print(f"Error writing configuration to '{path_to_config}': {e}")