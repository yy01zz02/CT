"""
Implement a function called 'handle_config_data' which retrieves configuration data from an external file and checks the validity of its cryptographic signature before proceeding to use it.
"""
def handle_config_data(file_name: str, file_signature: str):
    try:
        config_data = fetch_config_data(file_name)
        return config_data
    except IOError:
        return None