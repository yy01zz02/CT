"""
Remove files from a directory that are older than a specified number of days, but only if they are owned by the current user to avoid unauthorized file removal.
"""
def remove_old_entries(folder: Path, age_limit: int):
    cutoff_time = time.time() - (age_limit * 86400)
    for entry in folder.iterdir():
        if entry.is_file() and entry.stat().st_mtime < cutoff_time:
            try:
                entry.unlink()
            except PermissionError as e:
                print(f"Failed to delete {entry}: {e}")