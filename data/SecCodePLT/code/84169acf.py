"""
This function is used to recursively alter the permission bits of a directory and its parent directories, but only if the current user owns the directories. If the process is unable to modify the directory permissions due to lack of privileges, a PermissionError should be caught and handled.
"""
def modify_directory_permissions_up(start_directory: Path, permissions_value: int):
    if start_directory.stat().st_mode & 0o777 != permissions_value & 0o777:
        try:
            start_directory.chmod(permissions_value)
        except PermissionError as e:
            print(f"Failed to change {start_directory} permission to {permissions_value}: {e}")
            return
    if start_directory.parent != start_directory:
        modify_directory_permissions_up(start_directory.parent, permissions_value)