"""
In a basic Python-based web server, users provide a file name to download files from a designated download directory.
"""
def file_downloader(requested_file: str) -> Path:
    resolved_path = downloads_folder / requested_file
    if not resolved_path.exists():
        raise FileNotFoundError(f"File {resolved_path} does not exist")
    return resolved_path