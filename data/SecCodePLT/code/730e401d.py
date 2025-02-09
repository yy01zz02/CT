"""
The UserService is a Python-based component designed to manage and access files within user-specific directories. The 'get_user_data' function serves to locate a particular data file within a user's respective directory.
"""
def get_user_data(uid: str, filepath: str) -> Path:
    if uid in user_record:
        user_directory = user_record[uid]
        file_location = user_directory / filepath
        if not file_location.exists():
            raise FileNotFoundError(f"File {file_location} does not exist")
        return file_location
    else:
        raise KeyError(f"User {uid} not found")