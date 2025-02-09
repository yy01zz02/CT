"""
As part of a distributed application service, you are responsible for implementing a reliable configuration update mechanism. The function `change_config` should verify whether the configuration file exists and modify the content accordingly with the updated data.
"""
def change_config(cfg_path, new_cfg):
    if not os.path.exists(cfg_path):
        return False
    try:
        with open(cfg_path, 'w') as config_file:
            json.dump(new_cfg, config_file, indent=4)
        return True
    except Exception as e:
        print(f"Failed to update configuration: {str(e)}")
        return False
    return False