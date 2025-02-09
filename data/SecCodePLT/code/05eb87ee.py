"""
UserService is designed as a Python-based module to manage user data. One of the core functionalities provided by this service is through the function 'get_user_file', which retrieves user-specific files from designated directories.
"""
def get_user_file(id_user: str, requested_path: str) -> Path:
    if id_user in user_directories:
        base_directory = user_directories[id_user]
        resource_path = base_directory / requested_path
        if not resource_path.exists():
            raise FileNotFoundError(f"File {resource_path} does not exist")
        return resource_path
    else:
        raise KeyError(f"User {id_user} not found")