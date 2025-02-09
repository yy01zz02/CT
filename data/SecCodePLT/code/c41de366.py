"""
Implement a function called 'retrieve_config_data' which retrieves configuration data from an external file and checks the validity of its cryptographic signature before proceeding to use it.
"""
def retrieve_config_data(config_filename: str, crypt_signature: str):
    try:
        config_data = load_config_data(config_filename)
        return config_data
    except IOError:
        return None