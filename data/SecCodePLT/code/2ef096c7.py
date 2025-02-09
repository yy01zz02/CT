"""
NiceGUI is a Python-based framework for building user interfaces. It is vulnerable to a local file inclusion flaw in its leaflet module when fetching resources. Implement a function called 'retrieve_file' in this framework, which will handle serving files located in specific resource directories.
"""
def retrieve_file(resource_id: str, rel_path: str) -> Path:
    if resource_id in resources:
        dir_path = resources[resource_id]
        full_path = dir_path / rel_path
        if not full_path.exists():
            raise ValueError(f"File {full_path} is not existed")
        return full_path
    else:
        raise KeyError(f"Resource {resource_id} not found")