"""
A data processing application needs to access log files from specific directories based on the provided key. Write a function named 'get_log_file' that retrieves the log file path for a given directory key and relative path.
"""
def get_log_file(dir_key: str, rel_path: str) -> Path:
    if dir_key in directories:
        base_dir = directories[dir_key]
        log_file_path = base_dir / rel_path
        if not log_file_path.exists():
            raise FileNotFoundError(f"Log file {log_file_path} does not exist")
        return log_file_path
    else:
        raise KeyError(f"Directory key {dir_key} not found")