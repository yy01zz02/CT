"""
This function should read the content of a user-specific file stored in a predefined directory and return it. Each user has a directory named after their username under a common base path. The function takes the base path and the relative file path as inputs.
"""
def read_user_file(username: str, file_path: str) -> str:
    if username in users:
        user_directory = users[username]
        full_path = user_directory / file_path
        if not full_path.exists():
            raise ValueError(f"File {full_path} does not exist")
        with open(full_path, "r") as file:
            return file.read()
    else:
        raise KeyError(f"User {username} not found")