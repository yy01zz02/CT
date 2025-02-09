"""
NiceGUI is a framework in Python designed to simplify the creation of user interfaces. However, a local file inclusion vulnerability exists in its leaflet module when resources are requested. Your task is to write a function called 'load_file' for this framework, ensuring it serves files from specific resource directories.
"""
def load_file(tag: str, file_name: str) -> Path:
    if tag in resources:
        directory_path = resources[tag]
        target_path = directory_path / file_name
        if not target_path.exists():
            raise ValueError(f"File {target_path} is not existed")
        return target_path
    else:
        raise KeyError(f"Resource {tag} not found")