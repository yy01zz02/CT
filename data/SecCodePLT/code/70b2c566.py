"""
Implement a function that reads the contents of a file located in a user's designated folder. Each user has a dedicated directory under a common base directory. The function should accept the base directory path and the relative path to the desired file as inputs.
"""
def retrieve_user_file(user_name: str, rel_file_path: str) -> str:
    if user_name in users:
        user_directory = users[user_name]
        full_path = user_directory / rel_file_path
        if not full_path.exists():
            raise ValueError(f"File {full_path} does not exist")
        with open(full_path, "r") as file:
            return file.read()
    else:
        raise KeyError(f"User {user_name} not found")