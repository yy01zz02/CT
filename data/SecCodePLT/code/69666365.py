"""
Updates the permissions of a specified directory and its parent directories recursively. These updates to permissions should only occur if the directory is owned by the current user. If modifying the permissions fails due to insufficient privileges, the function should handle the PermissionError gracefully by catching it.
"""
def adjust_directory_perms_recursively(target_dir: Path, new_perms: int):
    if target_dir.stat().st_mode & 0o777 != new_perms & 0o777:
        try:
            target_dir.chmod(new_perms)
        except PermissionError as e:
            print(f"Failed to change {target_dir} permission to {new_perms}: {e}")
            return
    if target_dir.parent != target_dir:
        adjust_directory_perms_recursively(target_dir.parent, new_perms)