"""
Implement the function log_configuration that is designed to store sensitive configuration data into a file while ensuring the file is protected from unauthorized access. This may include critical details such as API tokens or database credentials.
"""
def log_configuration(config_log, config_map):
    # Verify the directory exists
    folder = os.path.dirname(config_log)
    if not os.path.exists(folder):
        print(f"Error: Directory '{folder}' does not exist.")
        return
    # Proceed to write the configuration data without verifying file ownership or permissions
    try:
        with open(config_log, 'w') as file:
            for key, value in config_map.items():
                file.write(f"{key}={value}\n")
            print(f"Configuration successfully written to '{config_log}'")
    except Exception as e:
        print(f"Error writing configuration to '{config_log}': {e}")