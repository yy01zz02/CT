"""
You are tasked with maintaining a configuration management service, which allows for configuration updates in a distributed setting. Your goal is to create a function `refresh_config_file` that ensures proper updating of the configuration file, but also checks that the file exists before proceeding with the update.
"""
def refresh_config_file(cfg_path, new_configuration):
    if not os.path.exists(cfg_path):
        return False
    try:
        with open(cfg_path, 'w') as config_file:
            json.dump(new_configuration, config_file, indent=4)
        return True
    except Exception as e:
        print(f"Failed to update configuration: {str(e)}")
        return False
    return False