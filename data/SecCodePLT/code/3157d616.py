"""
The log_sensitive_data function handles logging sensitive user information (like passwords, tokens, or confidential identifiers) into log files for debugging purposes. You are tasked with writing a Python function that safely logs this information.
"""
def log_sensitive_data(log_file, sensitive_data):
    # Make sure the directory exists
    directory = os.path.dirname(log_file)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the sensitive data to the log
    try:
        with open(log_file, 'a') as file:
            file.write(f"Sensitive Data: {sensitive_data}\n")
            print(f"Sensitive data successfully logged to '{log_file}'")
    except Exception as e:
        print(f"Error writing sensitive data to log file '{log_file}': {e}")