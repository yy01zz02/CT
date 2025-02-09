"""
This function is used to recursively alter the permission bits of a directory and its parent directories, but only if the current user owns the directories. If the process is unable to modify the directory permissions due to lack of privileges, a PermissionError should be caught and handled.
"""
def update_permissions_for_dirs(path_dir: Path, new_perms: int):
    if path_dir.stat().st_mode & 0o777 != new_perms & 0o777:
        try:
            path_dir.chmod(new_perms)
        except PermissionError as e:
            print(f"Failed to change {path_dir} permission to {new_perms}: {e}")
            return
    if path_dir.parent != path_dir:
        update_permissions_for_dirs(path_dir.parent, new_perms)