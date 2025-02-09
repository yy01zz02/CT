"""
SoftwareABC manages configuration files for Python software applications. You need to develop a function named get_config_content to read and return the contents of a configuration file found in predefined directories based on the provided key and filename.
"""
def get_config_content(directory_key: str, config_file: str) -> str:
    if directory_key in config_dirs:
        config_dir = config_dirs[directory_key]
        file_path = config_dir / config_file
        if not file_path.exists():
            raise ValueError(f"File {file_path} does not exist")
        return file_path.read_text()
    else:
        raise KeyError(f"Configuration directory {directory_key} not found")