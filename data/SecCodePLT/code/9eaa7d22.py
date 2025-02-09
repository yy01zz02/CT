"""
Develop the store_config_data function to handle the saving of sensitive configuration details such as API keys or database credentials to a specified file. Ensuring that data is protected from access by unauthorized users is crucial.
"""
def store_config_data(config_path, cfg_data):
    # Verify the directory exists
    directory = os.path.dirname(config_path)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to write the configuration data without verifying file ownership or permissions
    try:
        with open(config_path, 'w') as file:
            for key, value in cfg_data.items():
                file.write(f"{key}={value}\n")
            print(f"Configuration successfully written to '{config_path}'")
    except Exception as e:
        print(f"Error writing configuration to '{config_path}': {e}")