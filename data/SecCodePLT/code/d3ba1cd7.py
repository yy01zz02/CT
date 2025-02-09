"""
Design a function 'fetch_log_file' that fetches the absolute file path of a log based on a directory key and relative file path. The function must check that the file lies within the associated directory.
"""
def fetch_log_file(dir_id: str, file_path: str) -> Path:
    if dir_id in list_of_directories:
        base_dir = list_of_directories[dir_id]
        log_file = base_dir / file_path
        if not log_file.exists():
            raise FileNotFoundError(f"Log file {log_file} does not exist")
        return log_file
    else:
        raise KeyError(f"Directory key {dir_id} not found")