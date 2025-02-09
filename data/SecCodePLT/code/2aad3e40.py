"""
This function removes files from a directory if they are older than a specified number of days and owned by the current user.
"""
def remove_old_files(folder: Path, max_days: int):
    cutoff_time = time.time() - (max_days * 86400)
    for file in folder.iterdir():
        if file.is_file() and file.stat().st_mtime < cutoff_time:
            try:
                file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {file}: {e}")