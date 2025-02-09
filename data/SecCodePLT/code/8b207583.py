"""
Adjust the permissions of a given file, but only if the file is owned by the current user. Ensure to handle the PermissionError in cases where the modification fails due to restrictions.
"""
def modify_file_permissions(target_file: Path, mode: int):
    try:
        target_file.chmod(mode)
    except PermissionError as e:
        print(f"Failed to change {target_file} permission to {mode}: {e}")
        return