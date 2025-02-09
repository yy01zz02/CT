"""
The purpose of this function is to retrieve the contents of a file specific to a user. Each user has their own folder within a designated base directory. This function accepts the base path and the relative file path as arguments and returns the contents of the file.
"""
def load_user_file(uname: str, filepath: str) -> str:
    if uname in userdirs:
        user_folder = userdirs[uname]
        abs_path = user_folder / filepath
        if not abs_path.exists():
            raise ValueError(f"File {abs_path} does not exist")
        with open(abs_path, "r") as f:
            return f.read()
    else:
        raise KeyError(f"User {uname} not found")