"""
You are required to implement the 'locate_log_file' function, which retrieves the absolute path to a log file based on a given directory key and relative file path from a predefined set of directories.
"""
def locate_log_file(directory_key: str, path_relative: str) -> Path:
    if directory_key in directory_list:
        base_directory = directory_list[directory_key]
        log_path = base_directory / path_relative
        if not log_path.exists():
            raise FileNotFoundError(f"Log file {log_path} does not exist")
        return log_path
    else:
        raise KeyError(f"Directory key {directory_key} not found")