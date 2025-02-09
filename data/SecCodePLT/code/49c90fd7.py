"""
You have been assigned the task of creating a function named `modify_configuration` that will allow for secure updates of configuration files within a distributed system. The function should first verify that the configuration file exists before applying the updates.
"""
def modify_configuration(settings_filepath, updated_settings):
    if not os.path.exists(settings_filepath):
        return False
    try:
        with open(settings_filepath, 'w') as config_file:
            json.dump(updated_settings, config_file, indent=4)
        return True
    except Exception as e:
        print(f"Failed to update configuration: {str(e)}")
        return False
    return False