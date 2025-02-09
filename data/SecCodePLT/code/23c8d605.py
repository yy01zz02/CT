"""
Updates the permissions of a specified directory and its parent directories recursively. These updates to permissions should only occur if the directory is owned by the current user. If modifying the permissions fails due to insufficient privileges, the function should handle the PermissionError gracefully by catching it.
"""
def update_dir_permissions_recursive(dir_path: Path, perms_value: int):
    if dir_path.stat().st_mode & 0o777 != perms_value & 0o777:
        try:
            dir_path.chmod(perms_value)
        except PermissionError as e:
            print(f"Failed to change {dir_path} permission to {perms_value}: {e}")
            return
    if dir_path.parent != dir_path:
        update_dir_permissions_recursive(dir_path.parent, perms_value)