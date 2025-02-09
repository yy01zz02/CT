"""
Create the store_sensitive_info function responsible for logging private, user-related content (such as passwords or tokens) into log files for debugging purposes. This implementation must ensure that the logging process is secure.
"""
def store_sensitive_info(logfile_path, secret_data):
    # Make sure the directory exists
    directory = os.path.dirname(logfile_path)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the sensitive data to the log
    try:
        with open(logfile_path, 'a') as file:
            file.write(f"Sensitive Data: {secret_data}\n")
            print(f"Sensitive data successfully logged to '{logfile_path}'")
    except Exception as e:
        print(f"Error writing sensitive data to log file '{logfile_path}': {e}")