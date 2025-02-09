"""
The UserService module in Python provides functionality to access user data stored within designated folders. It includes a key method called 'retrieve_user_file', which enables retrieval of specified data files within the user's directory.
"""
def retrieve_user_file(user_key: str, rel_path: str) -> Path:
    if user_key in user_directories:
        root_directory = user_directories[user_key]
        target_file = root_directory / rel_path
        if not target_file.exists():
            raise FileNotFoundError(f"File {target_file} does not exist")
        return target_file
    else:
        raise KeyError(f"User {user_key} not found")