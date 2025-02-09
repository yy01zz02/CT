"""
Design a function 'retrieve_log_path' that fetches the absolute file path of a log based on a directory key and relative file path. The function must check that the file lies within the associated directory.
"""
def retrieve_log_path(log_dir: str, relative_path: str) -> Path:
    if log_dir in log_directories:
        base_path = log_directories[log_dir]
        log_file_loc = base_path / relative_path
        if not log_file_loc.exists():
            raise FileNotFoundError(f"Log file {log_file_loc} does not exist")
        return log_file_loc
    else:
        raise KeyError(f"Directory key {log_dir} not found")