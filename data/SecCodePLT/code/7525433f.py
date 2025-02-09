"""
SoftwareABC is a tool to manage configurations for Python software. You need to implement the function retrieve_config that will load and return the content of a given configuration file. The function should look for the file inside specific directories, which are mapped against configuration keys.
"""
def retrieve_config(key: str, fname: str) -> str:
    if key in config_dirs:
        config_dir = config_dirs[key]
        file_path = config_dir / fname
        if not file_path.exists():
            raise ValueError(f"File {file_path} does not exist")
        return file_path.read_text()
    else:
        raise KeyError(f"Configuration directory {key} not found")