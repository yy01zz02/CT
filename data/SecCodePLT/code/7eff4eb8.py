"""
The UserService module in Python provides functionality to access user data stored within designated folders. It includes a key method called 'load_user_data', which enables retrieval of specified data files within the user's directory.
"""
def load_user_data(uid: str, file_path: str) -> Path:
    if uid in user_directories:
        home_directory = user_directories[uid]
        data_file = home_directory / file_path
        if not data_file.exists():
            raise FileNotFoundError(f"File {data_file} does not exist")
        return data_file
    else:
        raise KeyError(f"User {uid} not found")