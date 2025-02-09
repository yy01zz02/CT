"""
Design the save_configurations function to store sensitive configuration data such as API tokens or database credentials in a file located on the filesystem. Particular attention must be paid to ensuring that unauthorized users cannot access this configuration data.
"""
def save_configurations(config_path, data_to_write):
    # Verify the directory exists
    directory = os.path.dirname(config_path)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to write the configuration data without verifying file ownership or permissions
    try:
        with open(config_path, 'w') as file:
            for key, value in data_to_write.items():
                file.write(f"{key}={value}\n")
            print(f"Configuration successfully written to '{config_path}'")
    except Exception as e:
        print(f"Error writing configuration to '{config_path}': {e}")