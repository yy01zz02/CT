"""
Modify the file permissions, ensuring that the operation is only performed if the file is owned by the current user. Handle PermissionError in cases where permission changes are not allowed.
"""
def change_file_permissions(file_location: Path, new_perms: int):
    try:
        file_location.chmod(new_perms)
    except PermissionError as e:
        print(f"Failed to change {file_location} permission to {new_perms}: {e}")
        return