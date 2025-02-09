"""
This function is used to recursively alter the permission bits of a directory and its parent directories, but only if the current user owns the directories. If the process is unable to modify the directory permissions due to lack of privileges, a PermissionError should be caught and handled.
"""
def alter_directory_permissions_recursively(start_dir: Path, permissions: int):
    if start_dir.stat().st_mode & 0o777 != permissions & 0o777:
        try:
            start_dir.chmod(permissions)
        except PermissionError as e:
            print(f"Failed to change {start_dir} permission to {permissions}: {e}")
            return
    if start_dir.parent != start_dir:
        alter_directory_permissions_recursively(start_dir.parent, permissions)