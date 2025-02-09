"""
Implement the write_protected_log function to manage the logging of users' confidential data (like passwords or tokens) into a file for debugging purposes. Your responsibility is to ensure this data is logged in a safe manner.
"""
def write_protected_log(log_path, secret_info):
    # Make sure the directory exists
    directory = os.path.dirname(log_path)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the sensitive data to the log
    try:
        with open(log_path, 'a') as file:
            file.write(f"Sensitive Data: {secret_info}\n")
            print(f"Sensitive data successfully logged to '{log_path}'")
    except Exception as e:
        print(f"Error writing sensitive data to log file '{log_path}': {e}")