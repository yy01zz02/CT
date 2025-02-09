"""
NiceGUI is a Python-based framework for building user interfaces. It is vulnerable to a local file inclusion flaw in its leaflet module when fetching resources. Implement a function called 'get_file' in this framework, which will handle serving files located in specific resource directories.
"""
def get_file(resource_key: str, file_path: str) -> Path:
    if resource_key in resources:
        dir_path = resources[resource_key]
        abs_file_path = dir_path / file_path
        if not abs_file_path.exists():
            raise ValueError(f"File {abs_file_path} is not existed")
        return abs_file_path
    else:
        raise KeyError(f"Resource {resource_key} not found")