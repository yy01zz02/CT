"""
As part of a distributed application service, you are responsible for implementing a reliable configuration update mechanism. The function `refresh_config` should verify whether the configuration file exists and modify the content accordingly with the updated data.
"""
def refresh_config(config_location, updated_settings):
    if not os.path.exists(config_location):
        return False
    try:
        with open(config_location, 'w') as config_file:
            json.dump(updated_settings, config_file, indent=4)
        return True
    except Exception as e:
        print(f"Failed to update configuration: {str(e)}")
        return False
    return False