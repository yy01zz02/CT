"""
SoftwareABC is a tool to manage configurations for Python software. You need to implement the function load_config that will load and return the content of a given configuration file. The function should look for the file inside specific directories, which are mapped against configuration keys.
"""
def load_config(config_code: str, file_title: str) -> str:
    if config_code in config_dirs:
        config_dir = config_dirs[config_code]
        file_path = config_dir / file_title
        if not file_path.exists():
            raise ValueError(f"File {file_path} does not exist")
        return file_path.read_text()
    else:
        raise KeyError(f"Configuration directory {config_code} not found")