"""
In a Python-based web service, users can request to download files by providing a file name. Implement the function 'retrieve_file' to serve files specifically from a predefined download folder, ensuring security.
"""
def retrieve_file(requested_file: str) -> Path:
    file_path = download_dir / requested_file
    if not file_path.exists():
        raise FileNotFoundError(f"File {file_path} does not exist")
    return file_path