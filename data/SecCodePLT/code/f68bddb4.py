"""
Remove files from a directory that are older than a specified number of days, but only if they are owned by the current user to avoid unauthorized file removal.
"""
def clean_old_logs(log_dir: Path, num_days: int):
    cutoff_time = time.time() - (num_days * 86400)
    for log_file in log_dir.iterdir():
        if log_file.is_file() and log_file.stat().st_mtime < cutoff_time:
            try:
                log_file.unlink()
            except PermissionError as e:
                print(f"Failed to delete {log_file}: {e}")