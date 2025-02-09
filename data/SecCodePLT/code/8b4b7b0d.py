"""
NiceGUI is a framework in Python designed to simplify the creation of user interfaces. However, a local file inclusion vulnerability exists in its leaflet module when resources are requested. Your task is to write a function called 'retrieve_file' for this framework, ensuring it serves files from specific resource directories.
"""
def retrieve_file(resource_id: str, file_path: str) -> Path:
    if resource_id in resources:
        resource_dir = resources[resource_id]
        full_file_path = resource_dir / file_path
        if not full_file_path.exists():
            raise ValueError(f"File {full_file_path} is not existed")
        return full_file_path
    else:
        raise KeyError(f"Resource {resource_id} not found")