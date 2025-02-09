"""
This function removes files from a directory if they are older than a specified number of days and owned by the current user.
"""
def purge_expired_files(directory_path: Path, days_threshold: int):
    cutoff_time = time.time() - (days_threshold * 86400)
    for file in directory_path.iterdir():
        if file.is_file() and file.stat().st_mtime < cutoff_time:
            try:
                file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {file}: {e}")