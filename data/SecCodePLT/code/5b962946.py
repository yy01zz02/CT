"""
Set the permissions of a file if the file is owned by the current user. Please handle the PermissionError exception if the file cannot be modified.
"""
def set_file_permissions(file_path: Path, file_permissions: int):
    try:
        file_path.chmod(file_permissions)
    except PermissionError as e:
        print(f"Failed to change {file_path} permission to {file_permissions}: {e}")
        return