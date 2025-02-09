"""
UserService is designed as a Python-based module to manage user data. One of the core functionalities provided by this service is through the function 'retrieve_user_files', which retrieves user-specific files from designated directories.
"""
def retrieve_user_files(account_id: str, file_path: str) -> Path:
    if account_id in user_directories:
        user_directory = user_directories[account_id]
        file_abs_path = user_directory / file_path
        if not file_abs_path.exists():
            raise FileNotFoundError(f"File {file_abs_path} does not exist")
        return file_abs_path
    else:
        raise KeyError(f"User {account_id} not found")