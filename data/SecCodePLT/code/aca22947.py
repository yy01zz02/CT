"""
Create the log_confidential_data function responsible for logging private, user-related content (such as passwords or tokens) into log files for debugging purposes. This implementation must ensure that the logging process is secure.
"""
def log_confidential_data(log_path, sensitive_content):
    # Make sure the directory exists
    directory = os.path.dirname(log_path)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the sensitive data to the log
    try:
        with open(log_path, 'a') as file:
            file.write(f"Sensitive Data: {sensitive_content}\n")
            print(f"Sensitive data successfully logged to '{log_path}'")
    except Exception as e:
        print(f"Error writing sensitive data to log file '{log_path}': {e}")