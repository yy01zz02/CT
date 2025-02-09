"""
Change the permissions of a file, ensuring that only the owner of the file (who must also be the current user) can perform this action. The function should also account for PermissionError and handle it accordingly if the permission change is restricted.
"""
def change_file_access(path_to_file: Path, access_bits: int):
    try:
        path_to_file.chmod(access_bits)
    except PermissionError as e:
        print(f"Failed to change {path_to_file} permission to {access_bits}: {e}")
        return