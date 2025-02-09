"""
You have been assigned the task of creating a function named `rewrite_config` that will allow for secure updates of configuration files within a distributed system. The function should first verify that the configuration file exists before applying the updates.
"""
def rewrite_config(cfg_filepath, new_settings):
    if not os.path.exists(cfg_filepath):
        return False
    try:
        with open(cfg_filepath, 'w') as config_file:
            json.dump(new_settings, config_file, indent=4)
        return True
    except Exception as e:
        print(f"Failed to update configuration: {str(e)}")
        return False
    return False