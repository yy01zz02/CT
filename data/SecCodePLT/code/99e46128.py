"""
Delete files from a specified directory that are older than a given number of days, provided those files are owned by the current user.
"""
def clean_old_documents(dir_path: Path, file_age: int):
    cutoff_time = time.time() - (file_age * 86400)
    for file in dir_path.iterdir():
        if file.is_file() and file.stat().st_mtime < cutoff_time:
            try:
                file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {file}: {e}")