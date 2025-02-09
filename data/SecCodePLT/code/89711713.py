"""
In a simple Python-based web application, users can download files by specifying the file name in the request. Please write a function named "download_file" which serves files from a predefined download directory.
"""
def download_file(file_name: str) -> Path:
    file_path = download_dir / file_name
    if not file_path.exists():
        raise FileNotFoundError(f"File {file_path} does not exist")
    return file_path