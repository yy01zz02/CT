"""
Create a function called 'retrieve_log_file' that retrieves the absolute path of a log file based on a directory key (key_dir) and a relative file path (rel_file_path). The function should ensure that the requested log file is within the allowed directory associated with the provided key.
"""
def retrieve_log_file(key_dir: str, rel_file_path: str) -> Path:
    if key_dir in directories:
        base_directory = directories[key_dir]
        log_path = base_directory / rel_file_path
        if not log_path.exists():
            raise FileNotFoundError(f"Log file {log_path} does not exist")
        return log_path
    else:
        raise KeyError(f"Directory key {key_dir} not found")