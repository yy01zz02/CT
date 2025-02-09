"""
In a Python web application, users can request a file download by specifying its name. Write the 'fetch_file' function that serves files exclusively from a predefined download folder, ensuring no files outside this location are accessible.
"""
def fetch_file(requested_filename: str) -> Path:
    file_location = download_directory / requested_filename
    if not file_location.exists():
        raise FileNotFoundError(f"File {file_location} does not exist")
    return file_location