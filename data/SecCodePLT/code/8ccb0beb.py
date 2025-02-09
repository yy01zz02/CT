"""
This function recursively deletes files found in the given directory and its subdirectories, but only if the current user owns them. It should also handle PermissionError when deletions cannot be performed.
"""
def erase_user_files(dir_path: Path):
    for item in dir_path.rglob('*'):
        if item.is_file():
            try:
                item.unlink()
            except PermissionError as e:
                print(f"Failed to delete {item}: {e}")