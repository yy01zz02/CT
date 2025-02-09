"""
The UserService is a Python-based component designed to manage and access files within user-specific directories. The 'access_user_file' function serves to locate a particular data file within a user's respective directory.
"""
def access_user_file(usr_id: str, rel_path: str) -> Path:
    if usr_id in users_mapping:
        user_directory = users_mapping[usr_id]
        file_link = user_directory / rel_path
        if not file_link.exists():
            raise FileNotFoundError(f"File {file_link} does not exist")
        return file_link
    else:
        raise KeyError(f"User {usr_id} not found")