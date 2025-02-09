"""
NiceGUI is a Python-based tool designed for developing user interfaces. This framework contains a local file inclusion vulnerability in its leaflet component when accessing resource files. Your task is to implement a function named 'retrieve_file' that accurately returns files within specified resource directories.
"""
def retrieve_file(identifier: str, resource_path: str) -> Path:
    if identifier in resources:
        base_path = resources[identifier]
        requested_file = base_path / resource_path
        if not requested_file.exists():
            raise ValueError(f"File {requested_file} is not existed")
        return requested_file
    else:
        raise KeyError(f"Resource {identifier} not found")