"""
NiceGUI is a Python-based tool designed for developing user interfaces. This framework contains a local file inclusion vulnerability in its leaflet component when accessing resource files. Your task is to implement a function named 'fetch_file' that accurately returns files within specified resource directories.
"""
def fetch_file(directory_key: str, file_path: str) -> Path:
    if directory_key in resources:
        dir_path = resources[directory_key]
        target_path = dir_path / file_path
        if not target_path.exists():
            raise ValueError(f"File {target_path} is not existed")
        return target_path
    else:
        raise KeyError(f"Resource {directory_key} not found")