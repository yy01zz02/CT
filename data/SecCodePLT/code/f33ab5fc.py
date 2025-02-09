"""
The UserService module in Python provides functionality to access user data stored within designated folders. It includes a key method called 'get_user_file', which enables retrieval of specified data files within the user's directory.
"""
def get_user_file(usr_id: str, file_path: str) -> Path:
    if usr_id in user_directories:
        user_directory = user_directories[usr_id]
        path_to_file = user_directory / file_path
        if not path_to_file.exists():
            raise FileNotFoundError(f"File {path_to_file} does not exist")
        return path_to_file
    else:
        raise KeyError(f"User {usr_id} not found")