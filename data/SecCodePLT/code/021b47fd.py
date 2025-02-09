"""
The UserService is a Python-based component designed to manage and access files within user-specific directories. The 'retrieve_profile_data' function serves to locate a particular data file within a user's respective directory.
"""
def retrieve_profile_data(profile_id: str, file_request: str) -> Path:
    if profile_id in user_profiles:
        user_directory = user_profiles[profile_id]
        file_path = user_directory / file_request
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist")
        return file_path
    else:
        raise KeyError(f"User {profile_id} not found")