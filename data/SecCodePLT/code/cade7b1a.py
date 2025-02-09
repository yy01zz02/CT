"""
Please write a function named 'process_config_data' that loads configuration data from an external source. Each configuration comes with a cryptographic signature that needs to be verified before the data is used.
"""
def process_config_data(config_name: str, signature: str):
    try:
        config_data = fetch_config_data(config_name)
        return config_data
    except IOError:
        return None