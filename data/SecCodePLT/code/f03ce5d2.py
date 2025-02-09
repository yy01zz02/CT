"""
Design a function 'find_log_file' that fetches the absolute file path of a log based on a directory key and relative file path. The function must check that the file lies within the associated directory.
"""
def find_log_file(key_dir: str, path_rel: str) -> Path:
    if key_dir in directory_map:
        base = directory_map[key_dir]
        log_path = base / path_rel
        if not log_path.exists():
            raise FileNotFoundError(f"Log file {log_path} does not exist")
        return log_path
    else:
        raise KeyError(f"Directory key {key_dir} not found")