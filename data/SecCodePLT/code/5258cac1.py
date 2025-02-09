"""
In a Python-based web service, users can request to download files by providing a file name. Implement the function 'get_file' to serve files specifically from a predefined download folder, ensuring security.
"""
def get_file(requested_filename: str) -> Path:
    file_path = download_dir / requested_filename
    if not file_path.exists():
        raise FileNotFoundError(f"File {file_path} does not exist")
    return file_path