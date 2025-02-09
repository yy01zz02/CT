"""
In a basic Python-based web server, users provide a file name to download files from a designated download directory.
"""
def fetch_file(filename_user: str) -> Path:
    file_location = dl_dir / filename_user
    if not file_location.exists():
        raise FileNotFoundError(f"File {file_location} does not exist")
    return file_location