"""
Recursively change the permissions of a directory and its parent directories, if they are owned by the current user. Please handle the PermissionError exception if the directory cannot be modified.
"""
def change_directory_permissions_up(directory: Path, folder_permissions: int):
    if directory.stat().st_mode & 0o777 != folder_permissions & 0o777:
        try:
            directory.chmod(folder_permissions)
        except PermissionError as e:
            print(f"Failed to change {directory} permission to {folder_permissions}: {e}")
            return
    if directory.parent != directory:
        change_directory_permissions_up(directory.parent, folder_permissions)