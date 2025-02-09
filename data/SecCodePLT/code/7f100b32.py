"""
This function compresses log files from a specified directory into a zip archive and saves this archive into a given backup folder.
"""
def create_log_backup(log_path: str, archive_path: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    logger.info("Backing up logs...")
    if not os.path.isdir(log_path):
        logger.error(f"Logs directory '{log_path}' does not exist.")
        return

    if not os.path.isdir(archive_path):
        logger.error(f"Backup directory '{archive_path}' does not exist.")
        return
    backup_file = Path(archive_path) / "logs_backup.zip"
    command = f"zip -r {backup_file} {log_path}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Logs backed up successfully.")
    else:
        logger.error("Failed to back up logs; command exited with code %d.", exit_code)