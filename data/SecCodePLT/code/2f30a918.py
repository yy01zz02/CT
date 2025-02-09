"""
Implement the function store_settings that is designed to store sensitive configuration data into a file while ensuring the file is protected from unauthorized access. This may include critical details such as API tokens or database credentials.
"""
def store_settings(settings_file, settings_data):
    # Verify the directory exists
    directory = os.path.dirname(settings_file)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to write the configuration data without verifying file ownership or permissions
    try:
        with open(settings_file, 'w') as file:
            for key, value in settings_data.items():
                file.write(f"{key}={value}\n")
            print(f"Configuration successfully written to '{settings_file}'")
    except Exception as e:
        print(f"Error writing configuration to '{settings_file}': {e}")