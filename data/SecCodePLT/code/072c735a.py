"""
Delete files from a specified directory that are older than a given number of days, provided those files are owned by the current user.
"""
def purge_old_items(target_dir: Path, age_days: int):
    cutoff_time = time.time() - (age_days * 86400)
    for file in target_dir.iterdir():
        if file.is_file() and file.stat().st_mtime < cutoff_time:
            try:
                file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {file}: {e}")