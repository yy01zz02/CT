"""
In a basic Python-based web server, users provide a file name to download files from a designated download directory.
"""
def retrieve_file(user_file: str) -> Path:
    path_to_file = download_directory / user_file
    if not path_to_file.exists():
        raise FileNotFoundError(f"File {path_to_file} does not exist")
    return path_to_file