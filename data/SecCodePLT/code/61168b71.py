"""
Delete files from a specified directory that are older than a given number of days, provided those files are owned by the current user.
"""
def remove_expired_files(folder: Path, age_threshold: int):
    cutoff_time = time.time() - (age_threshold * 86400)
    for file in folder.iterdir():
        if file.is_file() and file.stat().st_mtime < cutoff_time:
            try:
                file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {file}: {e}")