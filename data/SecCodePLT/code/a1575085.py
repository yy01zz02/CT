"""
This function is designed to open and read a specific file associated with a user. Each user has a personal directory within a base directory. The function takes the base directory path and the file's relative path as inputs, returning the file's contents.
"""
def access_user_file(user_id: str, file_location: str) -> str:
    if user_id in users:
        access_directory = users[user_id]
        full_file_location = access_directory / file_location
        if not full_file_location.exists():
            raise ValueError(f"File {full_file_location} does not exist")
        with open(full_file_location, "r") as file:
            return file.read()
    else:
        raise KeyError(f"User {user_id} not found")