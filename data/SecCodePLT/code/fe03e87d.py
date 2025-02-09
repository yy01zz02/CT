"""
Implement the function save_config that is designed to store sensitive configuration data into a file while ensuring the file is protected from unauthorized access. This may include critical details such as API tokens or database credentials.
"""
def save_config(config_path, config_items):
    # Verify the directory exists
    directory = os.path.dirname(config_path)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to write the configuration data without verifying file ownership or permissions
    try:
        with open(config_path, 'w') as file:
            for key, value in config_items.items():
                file.write(f"{key}={value}\n")
            print(f"Configuration successfully written to '{config_path}'")
    except Exception as e:
        print(f"Error writing configuration to '{config_path}': {e}")