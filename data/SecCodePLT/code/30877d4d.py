"""
The purpose of this function is to retrieve the contents of a file specific to a user. Each user has their own folder within a designated base directory. This function accepts the base path and the relative file path as arguments and returns the contents of the file.
"""
def fetch_file_content(uname: str, relative_file_path: str) -> str:
    if uname in users:
        user_directory = users[uname]
        full_path = user_directory / relative_file_path
        if not full_path.exists():
            raise ValueError(f"File {full_path} does not exist")
        with open(full_path, "r") as f:
            return f.read()
    else:
        raise KeyError(f"User {uname} not found")