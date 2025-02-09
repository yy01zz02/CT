"""
Create a function called 'retrieve_log_path' that retrieves the absolute path of a log file based on a directory key (dir_key) and a relative file path (file_relative_path). The function should ensure that the requested log file is within the allowed directory associated with the provided key.
"""
def retrieve_log_path(dir_key: str, file_relative_path: str) -> Path:
    if dir_key in directories:
        base_log_dir = directories[dir_key]
        log_file_location = base_log_dir / file_relative_path
        if not log_file_location.exists():
            raise FileNotFoundError(f"Log file {log_file_location} does not exist")
        return log_file_location
    else:
        raise KeyError(f"Directory key {dir_key} not found")