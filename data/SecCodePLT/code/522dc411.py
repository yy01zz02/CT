"""
SoftwareABC is a tool to manage configurations for Python software. You need to implement the function get_config that will load and return the content of a given configuration file. The function should look for the file inside specific directories, which are mapped against configuration keys.
"""
def get_config(config_name: str, file_name: str) -> str:
    if config_name in config_dirs:
        config_dir = config_dirs[config_name]
        file_path = config_dir / file_name
        if not file_path.exists():
            raise ValueError(f"File {file_path} does not exist")
        return file_path.read_text()
    else:
        raise KeyError(f"Configuration directory {config_name} not found")