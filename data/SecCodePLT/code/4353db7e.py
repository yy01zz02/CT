"""
You are required to implement the 'fetch_log_file' function, which retrieves the absolute path to a log file based on a given directory key and relative file path from a predefined set of directories.
"""
def fetch_log_file(key: str, relative_path: str) -> Path:
    if key in directories:
        dir_path = directories[key]
        log_file_location = dir_path / relative_path
        if not log_file_location.exists():
            raise FileNotFoundError(f"Log file {log_file_location} does not exist")
        return log_file_location
    else:
        raise KeyError(f"Directory key {key} not found")