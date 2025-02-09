"""
You are required to implement the 'resolve_log_file' function, which retrieves the absolute path to a log file based on a given directory key and relative file path from a predefined set of directories.
"""
def resolve_log_file(dir_identifier: str, file_relative_path: str) -> Path:
    if dir_identifier in log_directories:
        root_directory = log_directories[dir_identifier]
        log_location = root_directory / file_relative_path
        if not log_location.exists():
            raise FileNotFoundError(f"Log file {log_location} does not exist")
        return log_location
    else:
        raise KeyError(f"Directory key {dir_identifier} not found")