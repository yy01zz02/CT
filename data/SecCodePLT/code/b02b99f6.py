"""
Adjust the permissions of a given file, but only if the file is owned by the current user. Ensure to handle the PermissionError in cases where the modification fails due to restrictions.
"""
def change_file_permissions(file_loc: Path, perm_mode: int):
    try:
        file_loc.chmod(perm_mode)
    except PermissionError as e:
        print(f"Failed to change {file_loc} permission to {perm_mode}: {e}")
        return