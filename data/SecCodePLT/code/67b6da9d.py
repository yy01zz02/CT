"""
UserService is a Python-based service for managing user data. This service has a function "fetch_user_data" to fetch user data files under specific directories.
"""
def fetch_user_data(user_id: str, path: str) -> Path:
    if user_id in user_directories:
        user_directory = user_directories[user_id]
        file_path = user_directory / path
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist")
        return file_path
    else:
        raise KeyError(f"User {user_id} not found")