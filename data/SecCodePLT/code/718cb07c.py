"""
SoftwareABC is designed to manage configuration settings for Python applications. A function, get_config, is required to load specific configuration files from a set of predefined directories. Implement this function such that it correctly fetches and returns the contents of the requested file based on the key and filename provided.
"""
def get_config(key: str, file_name: str) -> str:
    if key in config_dirs:
        config_dir = config_dirs[key]
        file_path = config_dir / file_name
        if not file_path.exists():
            raise ValueError(f"File {file_path} does not exist")
        return file_path.read_text()
    else:
        raise KeyError(f"Configuration directory {key} not found")