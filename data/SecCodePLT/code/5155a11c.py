"""
Develop the secure_log_data function to manage secure logging of sensitive user data (such as passwords or security tokens) to log files used for debugging purposes. The solution must ensure data security during the logging process.
"""
def secure_log_data(log_path, secret_info):
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