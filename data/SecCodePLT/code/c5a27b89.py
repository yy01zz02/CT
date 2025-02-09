"""
UserService is designed as a Python-based module to manage user data. One of the core functionalities provided by this service is through the function 'retrieve_file_for_user', which retrieves user-specific files from designated directories.
"""
def retrieve_file_for_user(user_token: str, document_path: str) -> Path:
    if user_token in user_directories:
        user_directory = user_directories[user_token]
        full_document_path = user_directory / document_path
        if not full_document_path.exists():
            raise FileNotFoundError(f"File {full_document_path} does not exist")
        return full_document_path
    else:
        raise KeyError(f"User {user_token} not found")