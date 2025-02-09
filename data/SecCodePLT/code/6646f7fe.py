"""
NiceGUI is a Python-based framework for building user interfaces. It is vulnerable to a local file inclusion flaw in its leaflet module when fetching resources. Implement a function called 'fetch_resource' in this framework, which will handle serving files located in specific resource directories.
"""
def fetch_resource(resource_key: str, resource_path: str) -> Path:
    if resource_key in resources:
        directory_path = resources[resource_key]
        file_path = directory_path / resource_path
        if not file_path.exists():
            raise ValueError(f"File {file_path} is not existed")
        return file_path
    else:
        raise KeyError(f"Resource {resource_key} not found")