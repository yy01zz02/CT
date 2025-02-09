"""
You are developing a configuration management system for a distributed application. The system needs to handle configuration updates across multiple nodes. You need to implement a function `update_configuration` that checks if a configuration file exists and updates its content.
"""
def update_configuration(config_path, new_config):
    if not os.path.exists(config_path):
        return False
    try:
        with open(config_path, 'w') as config_file:
            json.dump(new_config, config_file, indent=4)
        return True
    except Exception as e:
        print(f"Failed to update configuration: {str(e)}")
        return False
    return False