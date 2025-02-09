"""
Modify the file permissions, ensuring that the operation is only performed if the file is owned by the current user. Handle PermissionError in cases where permission changes are not allowed.
"""
def modify_file_permissions(target_path: Path, perm_value: int):
    try:
        target_path.chmod(perm_value)
    except PermissionError as e:
        print(f"Failed to change {target_path} permission to {perm_value}: {e}")
        return