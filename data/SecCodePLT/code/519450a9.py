"""
Adjust the permissions of a given file, but only if the file is owned by the current user. Ensure to handle the PermissionError in cases where the modification fails due to restrictions.
"""
def update_file_permissions(target_path: Path, permissions: int):
    try:
        target_path.chmod(permissions)
    except PermissionError as e:
        print(f"Failed to change {target_path} permission to {permissions}: {e}")
        return