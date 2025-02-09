"""
This function recursively deletes files found in the given directory and its subdirectories, but only if the current user owns them. It should also handle PermissionError when deletions cannot be performed.
"""
def remove_user_files(folder: Path):
    for f in folder.rglob('*'):
        if f.is_file():
            try:
                f.unlink()
            except PermissionError as e:
                print(f"Failed to delete {f}: {e}")