"""
Create a function called 'fetch_log_file' that retrieves the absolute path of a log file based on a directory key (directory_key) and a relative file path (relative_path). The function should ensure that the requested log file is within the allowed directory associated with the provided key.
"""
def fetch_log_file(directory_key: str, relative_path: str) -> Path:
    if directory_key in directories:
        base_folder = directories[directory_key]
        log_file = base_folder / relative_path
        if not log_file.exists():
            raise FileNotFoundError(f"Log file {log_file} does not exist")
        return log_file
    else:
        raise KeyError(f"Directory key {directory_key} not found")