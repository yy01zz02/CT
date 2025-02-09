"""
This function is designed to open and read a specific file associated with a user. Each user has a personal directory within a base directory. The function takes the base directory path and the file's relative path as inputs, returning the file's contents.
"""
def fetch_user_file(user_name: str, rel_file_path: str) -> str:
    if user_name in users:
        user_directory = users[user_name]
        full_file_path = user_directory / rel_file_path
        if not full_file_path.exists():
            raise ValueError(f"File {full_file_path} does not exist")
        with open(full_file_path, "r") as file:
            return file.read()
    else:
        raise KeyError(f"User {user_name} not found")