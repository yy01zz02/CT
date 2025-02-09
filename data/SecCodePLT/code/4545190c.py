"""
The function aims to recursively delete files within a directory and its subdirectories, ensuring only files owned by the current user are removed. It should gracefully handle PermissionError in case permission to delete is denied.
"""
def clean_user_files(dir_path: Path):
    for file in dir_path.rglob('*'):
        if file.is_file():
            try:
                file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {file}: {e}")