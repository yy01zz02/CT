"""
As part of a distributed application service, you are responsible for implementing a reliable configuration update mechanism. The function `modify_config` should verify whether the configuration file exists and modify the content accordingly with the updated data.
"""
def modify_config(path_to_config, updated_config):
    if not os.path.exists(path_to_config):
        return False
    try:
        with open(path_to_config, 'w') as config_file:
            json.dump(updated_config, config_file, indent=4)
        return True
    except Exception as e:
        print(f"Failed to update configuration: {str(e)}")
        return False
    return False