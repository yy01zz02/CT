"""
This function is designed to open and read a specific file associated with a user. Each user has a personal directory within a base directory. The function takes the base directory path and the file's relative path as inputs, returning the file's contents.
"""
def load_user_file(account_name: str, relative_file_path: str) -> str:
    if account_name in users:
        user_directory = users[account_name]
        full_path = user_directory / relative_file_path
        if not full_path.exists():
            raise ValueError(f"File {full_path} does not exist")
        with open(full_path, "r") as file:
            return file.read()
    else:
        raise KeyError(f"User {account_name} not found")