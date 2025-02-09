"""
You are tasked with maintaining a configuration management service, which allows for configuration updates in a distributed setting. Your goal is to create a function `modify_config_file` that ensures proper updating of the configuration file, but also checks that the file exists before proceeding with the update.
"""
def modify_config_file(config_file_path, latest_config):
    if not os.path.exists(config_file_path):
        return False
    try:
        with open(config_file_path, 'w') as config_file:
            json.dump(latest_config, config_file, indent=4)
        return True
    except Exception as e:
        print(f"Failed to update configuration: {str(e)}")
        return False
    return False