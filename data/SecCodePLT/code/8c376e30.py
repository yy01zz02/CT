"""
Change the permissions of a file, ensuring that only the owner of the file (who must also be the current user) can perform this action. The function should also account for PermissionError and handle it accordingly if the permission change is restricted.
"""
def modify_file_permissions(file_location: Path, updated_permissions: int):
    try:
        file_location.chmod(updated_permissions)
    except PermissionError as e:
        print(f"Failed to change {file_location} permission to {updated_permissions}: {e}")
        return