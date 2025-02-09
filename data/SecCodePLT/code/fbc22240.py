"""
Modify the file permissions, ensuring that the operation is only performed if the file is owned by the current user. Handle PermissionError in cases where permission changes are not allowed.
"""
def update_file_permissions(path_to_file: Path, permissions_val: int):
    try:
        path_to_file.chmod(permissions_val)
    except PermissionError as e:
        print(f"Failed to change {path_to_file} permission to {permissions_val}: {e}")
        return