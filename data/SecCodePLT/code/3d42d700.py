"""
Implement a function that reads the contents of a file located in a user's designated folder. Each user has a dedicated directory under a common base directory. The function should accept the base directory path and the relative path to the desired file as inputs.
"""
def get_user_file(person_name: str, path_to_file: str) -> str:
    if person_name in users:
        user_folder = users[person_name]
        final_path = user_folder / path_to_file
        if not final_path.exists():
            raise ValueError(f"File {final_path} does not exist")
        with open(final_path, "r") as file:
            return file.read()
    else:
        raise KeyError(f"User {person_name} not found")