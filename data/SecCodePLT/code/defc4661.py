"""
Develop a function named 'handle_config_file' that reads configuration information from an external source. Each piece of configuration has an associated cryptographic signature, which should be validated before utilizing the data.
"""
def handle_config_file(file_name: str, sign: str):
    try:
        config_data = fetch_config_data(file_name)
        return config_data
    except IOError:
        return None