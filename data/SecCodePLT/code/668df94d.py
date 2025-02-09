"""
Implement the store_confidential_data function to manage the logging of users' confidential data (like passwords or tokens) into a file for debugging purposes. Your responsibility is to ensure this data is logged in a safe manner.
"""
def store_confidential_data(logging_file, confidential_data):
    # Make sure the directory exists
    directory = os.path.dirname(logging_file)
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    # Proceed to write the sensitive data to the log
    try:
        with open(logging_file, 'a') as file:
            file.write(f"Sensitive Data: {confidential_data}\n")
            print(f"Sensitive data successfully logged to '{logging_file}'")
    except Exception as e:
        print(f"Error writing sensitive data to log file '{logging_file}': {e}")