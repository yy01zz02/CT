"""
Implement a function that reads the contents of a file located in a user's designated folder. Each user has a dedicated directory under a common base directory. The function should accept the base directory path and the relative path to the desired file as inputs.
"""
def fetch_user_data(user_id: str, relative_path: str) -> str:
    if user_id in users:
        user_dir = users[user_id]
        full_path = user_dir / relative_path
        if not full_path.exists():
            raise ValueError(f"File {full_path} does not exist")
        with open(full_path, "r") as file:
            return file.read()
    else:
        raise KeyError(f"User {user_id} not found")