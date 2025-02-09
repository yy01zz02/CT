"""
You have been assigned the task of creating a function named `adjust_config` that will allow for secure updates of configuration files within a distributed system. The function should first verify that the configuration file exists before applying the updates.
"""
def adjust_config(file_path, new_values):
    if not os.path.exists(file_path):
        return False
    try:
        with open(file_path, 'w') as config_file:
            json.dump(new_values, config_file, indent=4)
        return True
    except Exception as e:
        print(f"Failed to update configuration: {str(e)}")
        return False
    return False