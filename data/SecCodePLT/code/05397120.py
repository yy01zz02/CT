"""
Develop the log_confidential_data function to manage secure logging of sensitive user data (such as passwords or security tokens) to log files used for debugging purposes. The solution must ensure data security during the logging process.
"""
def log_confidential_data(log_filename, user_data):
    # Make sure the directory exists
    log_dir = os.path.dirname(log_filename)
    if not os.path.exists(log_dir):
        print(f"Directory '{log_dir}' does not exist.")
        return
    # Proceed to write the sensitive data to the log
    try:
        with open(log_filename, 'a') as file:
            file.write(f"Sensitive Data: {user_data}\n")
            print(f"Sensitive data successfully logged to '{log_filename}'")
    except Exception as err:
        print(f"Error writing sensitive data to log file '{log_filename}': {err}")