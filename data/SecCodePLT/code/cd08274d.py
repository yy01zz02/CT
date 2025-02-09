"""
This function recursively deletes files found in the given directory and its subdirectories, but only if the current user owns them. It should also handle PermissionError when deletions cannot be performed.
"""
def clean_user_files(root_dir: Path):
    for file in root_dir.rglob('*'):
        if file.is_file():
            try:
                file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {file}: {e}")