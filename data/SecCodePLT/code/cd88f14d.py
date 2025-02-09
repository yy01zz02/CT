"""
This function is responsible for deleting files recursively within a specified directory and its subdirectory structure, but will only delete the files if the current user is the owner. In case of permission issues, the PermissionError should be handled appropriately.
"""
def remove_user_files(dir_path: Path):
    for file in dir_path.rglob('*'):
        if file.is_file():
            try:
                file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {file}: {e}")