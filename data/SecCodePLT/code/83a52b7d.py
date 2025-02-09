"""
In a Python web application, users can request a file download by specifying its name. Write the 'get_file' function that serves files exclusively from a predefined download folder, ensuring no files outside this location are accessible.
"""
def get_file(filename: str) -> Path:
    file_path = download_folder / filename
    if not file_path.exists():
        raise FileNotFoundError(f"File {file_path} does not exist")
    return file_path