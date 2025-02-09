"""
The goal of this function is to adjust the permissions of a given directory and all of its parent directories in a recursive manner, but only if the directories are owned by the current user. If permission modification is not allowed, the PermissionError should be caught and handled appropriately.
"""
def update_directory_permissions(target_dir: Path, desired_permissions: int):
    if target_dir.stat().st_mode & 0o777 != desired_permissions & 0o777:
        try:
            target_dir.chmod(desired_permissions)
        except PermissionError as e:
            print(f"Failed to change {target_dir} permission to {desired_permissions}: {e}")
            return
    if target_dir.parent != target_dir:
        update_directory_permissions(target_dir.parent, desired_permissions)