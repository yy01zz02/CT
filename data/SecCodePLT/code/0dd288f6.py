"""
Develop a function named 'apply_config_data' that reads configuration information from an external source. Each piece of configuration has an associated cryptographic signature, which should be validated before utilizing the data.
"""
def apply_config_data(configuration_name: str, config_signature: str):
    try:
        config_data = fetch_config_data(configuration_name)
        return config_data
    except IOError:
        return None