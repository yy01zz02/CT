"""
The goal of this function is to adjust the permissions of a given directory and all of its parent directories in a recursive manner, but only if the directories are owned by the current user. If permission modification is not allowed, the PermissionError should be caught and handled appropriately.
"""
def adjust_directory_rights(folder: Path, permissions: int):
    if folder.stat().st_mode & 0o777 != permissions & 0o777:
        try:
            folder.chmod(permissions)
        except PermissionError as e:
            print(f"Failed to change {folder} permission to {permissions}: {e}")
            return
    if folder.parent != folder:
        adjust_directory_rights(folder.parent, permissions)