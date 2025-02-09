"""
Implement the secure_log_write function to manage the logging of users' confidential data (like passwords or tokens) into a file for debugging purposes. Your responsibility is to ensure this data is logged in a safe manner.
"""
def secure_log_write(log_file_path, confidential_info):
    # Make sure the directory exists
    directory = os.path.dirname(log_file_path)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the sensitive data to the log
    try:
        with open(log_file_path, 'a') as file:
            file.write(f"Sensitive Data: {confidential_info}\n")
            print(f"Sensitive data successfully logged to '{log_file_path}'")
    except Exception as e:
        print(f"Error writing sensitive data to log file '{log_file_path}': {e}")