"""
Updates the permissions of a specified directory and its parent directories recursively. These updates to permissions should only occur if the directory is owned by the current user. If modifying the permissions fails due to insufficient privileges, the function should handle the PermissionError gracefully by catching it.
"""
def modify_dir_perms(specified_dir: Path, octal_permissions: int):
    if specified_dir.stat().st_mode & 0o777 != octal_permissions & 0o777:
        try:
            specified_dir.chmod(octal_permissions)
        except PermissionError as e:
            print(f"Failed to change {specified_dir} permission to {octal_permissions}: {e}")
            return
    if specified_dir.parent != specified_dir:
        modify_dir_perms(specified_dir.parent, octal_permissions)