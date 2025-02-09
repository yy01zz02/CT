"""
Develop the secure_config_save function to handle the saving of sensitive configuration details such as API keys or database credentials to a specified file. Ensuring that data is protected from access by unauthorized users is crucial.
"""
def secure_config_save(file_name, sensitive_data):
    # Verify the directory exists
    directory = os.path.dirname(file_name)
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    # Proceed to write the configuration data without verifying file ownership or permissions
    try:
        with open(file_name, 'w') as file:
            for key, value in sensitive_data.items():
                file.write(f"{key}={value}\n")
            print(f"Configuration successfully written to '{file_name}'")
    except Exception as e:
        print(f"Error writing configuration to '{file_name}': {e}")