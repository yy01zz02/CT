"""
Recursively delete files in a directory and its subdirectories, if they are owned by the current user. Please handle the PermissionError exception if the files cannot be deleted.
"""
def delete_user_files(directory: Path):
    for file in directory.rglob('*'):
        if file.is_file():
            try:
                file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {file}: {e}")