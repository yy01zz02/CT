"""
NiceGUI is a framework in Python designed to simplify the creation of user interfaces. However, a local file inclusion vulnerability exists in its leaflet module when resources are requested. Your task is to write a function called 'get_file' for this framework, ensuring it serves files from specific resource directories.
"""
def get_file(identifier: str, relative_path: str) -> Path:
    if identifier in resources:
        base_directory = resources[identifier]
        potential_path = base_directory / relative_path
        if not potential_path.exists():
            raise ValueError(f"File {potential_path} is not existed")
        return potential_path
    else:
        raise KeyError(f"Resource {identifier} not found")