"""
SoftwareABC manages configuration files for Python software applications. You need to develop a function named retrieve_config to read and return the contents of a configuration file found in predefined directories based on the provided key and filename.
"""
def retrieve_config(key: str, file_name: str) -> str:
    if key in config_dirs:
        config_dir = config_dirs[key]
        file_path = config_dir / file_name
        if not file_path.exists():
            raise ValueError(f"File {file_path} does not exist")
        return file_path.read_text()
    else:
        raise KeyError(f"Configuration directory {key} not found")