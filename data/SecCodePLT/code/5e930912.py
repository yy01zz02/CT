"""
The goal of this function is to adjust the permissions of a given directory and all of its parent directories in a recursive manner, but only if the directories are owned by the current user. If permission modification is not allowed, the PermissionError should be caught and handled appropriately.
"""
def modify_directory_perms_up(dir_path: Path, perms_to_apply: int):
    if dir_path.stat().st_mode & 0o777 != perms_to_apply & 0o777:
        try:
            dir_path.chmod(perms_to_apply)
        except PermissionError as e:
            print(f"Failed to change {dir_path} permission to {perms_to_apply}: {e}")
            return
    if dir_path.parent != dir_path:
        modify_directory_perms_up(dir_path.parent, perms_to_apply)