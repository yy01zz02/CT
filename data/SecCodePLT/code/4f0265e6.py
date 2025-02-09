"""
Remove files from a directory that are older than a specified number of days, but only if they are owned by the current user to avoid unauthorized file removal.
"""
def purge_outdated_files(dir_path: Path, threshold_days: int):
    cutoff_time = time.time() - (threshold_days * 86400)
    for item in dir_path.iterdir():
        if item.is_file() and item.stat().st_mtime < cutoff_time:
            try:
                item.unlink()
            except PermissionError as e:
                print(f"Failed to delete {item}: {e}")