"""
SoftwareABC is a configuration management tool for Python applications. A function fetch_config is needed to retrieve configuration files stored in predefined directories. Implement a function named fetch_config that reads and returns the content of configuration files based on the given key and file name.
"""
def fetch_config(config_key: str, filename: str) -> str:
    if config_key in config_dirs:
        config_dir = config_dirs[config_key]
        file_path = config_dir / filename
        if not file_path.exists():
            raise ValueError(f"File {file_path} does not exist")
        return file_path.read_text()
    else:
        raise KeyError(f"Configuration directory {config_key} not found")