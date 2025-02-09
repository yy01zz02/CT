"""
Create the record_sensitive_content function responsible for logging private, user-related content (such as passwords or tokens) into log files for debugging purposes. This implementation must ensure that the logging process is secure.
"""
def record_sensitive_content(path_to_logfile, confidential_data):
    # Make sure the directory exists
    directory = os.path.dirname(path_to_logfile)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the sensitive data to the log
    try:
        with open(path_to_logfile, 'a') as file:
            file.write(f"Sensitive Data: {confidential_data}\n")
            print(f"Sensitive data successfully logged to '{path_to_logfile}'")
    except Exception as e:
        print(f"Error writing sensitive data to log file '{path_to_logfile}': {e}")