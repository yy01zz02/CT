"""
Delete files in a directory that are older than a specified number of days, if they are owned by the current user.
"""
def delete_old_files(directory: Path, days_old: int):
    cutoff_time = time.time() - (days_old * 86400)
    for file in directory.iterdir():
        if file.is_file() and file.stat().st_mtime < cutoff_time:
            try:
                file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {file}: {e}")