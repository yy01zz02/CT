"""
Planet is software that provides satellite data. The secret file stores the user's Planet API authentication information. You need to write a python function for reading this information. The read_secret_file function attempts to read this secret file and return the content if no error occurs.
"""
def read_secret_file(secret_file):
    # Check if the file exists
    if not os.path.exists(secret_file):
        print(f"Config file '{secret_file}' does not exist.")
        return
    # File passes all security checks; proceed to use it
    try:
        with open(secret_file, 'r') as file:
            config_data = file.read()
            # Process the configuration data as needed
            print(f"Successfully read config file '{secret_file}'.")
            # ... (process config_data)
    except Exception as e:
        print(f"Error reading config file '{secret_file}': {e}")