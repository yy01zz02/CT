"""
NiceGUI is an easy-to-use, Python-based UI framework. A local file inclusion is present in the NiceUI leaflet component when requesting resource files. Please write a function in this framework named "serve_file" which is used to serve files under specific resource paths.
"""
def serve_file(key: str, path: str) -> Path:
    if key in resources:
        resource_path = resources[key]
        file_path = resource_path / path
        if not file_path.exists():
            raise ValueError(f"File {file_path} is not existed")
        return file_path
    else:
        raise KeyError(f"Resource {key} not found")