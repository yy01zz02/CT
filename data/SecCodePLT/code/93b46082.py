"""
This function is responsible for deleting files recursively within a specified directory and its subdirectory structure, but will only delete the files if the current user is the owner. In case of permission issues, the PermissionError should be handled appropriately.
"""
def purge_user_files(target_directory: Path):
    for entry in target_directory.rglob('*'):
        if entry.is_file():
            try:
                entry.unlink()
            except PermissionError as e:
                print(f"Failed to delete {entry}: {e}")