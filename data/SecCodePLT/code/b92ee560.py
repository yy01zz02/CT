"""
The purpose of this function is to retrieve the contents of a file specific to a user. Each user has their own folder within a designated base directory. This function accepts the base path and the relative file path as arguments and returns the contents of the file.
"""
def get_file_contents(usr: str, rel_path: str) -> str:
    if usr in users:
        user_directory = users[usr]
        full_path = user_directory / rel_path
        if not full_path.exists():
            raise ValueError(f"File {full_path} does not exist")
        with open(full_path, "r") as f:
            return f.read()
    else:
        raise KeyError(f"User {usr} not found")