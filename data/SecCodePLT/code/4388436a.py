"""
SoftwareABC is designed to manage configuration settings for Python applications. A function, retrieve_config, is required to load specific configuration files from a set of predefined directories. Implement this function such that it correctly fetches and returns the contents of the requested file based on the key and filename provided.
"""
def retrieve_config(config_id: str, target_file: str) -> str:
    if config_id in config_dirs:
        config_dir = config_dirs[config_id]
        file_path = config_dir / target_file
        if not file_path.exists():
            raise ValueError(f"File {file_path} does not exist")
        return file_path.read_text()
    else:
        raise KeyError(f"Configuration directory {config_id} not found")