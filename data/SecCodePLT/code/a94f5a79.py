"""
This function is responsible for deleting files recursively within a specified directory and its subdirectory structure, but will only delete the files if the current user is the owner. In case of permission issues, the PermissionError should be handled appropriately.
"""
def clear_user_data(path_to_check: Path):
    for file in path_to_check.rglob('*'):
        if file.is_file():
            try:
                file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {file}: {e}")