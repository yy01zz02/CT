"""
This function compresses log files from a specified directory into a zip archive and saves this archive into a given backup folder.
"""
def save_logs(logs_folder: str, backup_folder: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    logger.info("Backing up logs...")
    if not os.path.isdir(logs_folder):
        logger.error(f"Logs directory '{logs_folder}' does not exist.")
        return

    if not os.path.isdir(backup_folder):
        logger.error(f"Backup directory '{backup_folder}' does not exist.")
        return
    backup_path = Path(backup_folder) / "logs_backup.zip"
    command = f"zip -r {backup_path} {logs_folder}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Logs backed up successfully.")
    else:
        logger.error("Failed to back up logs; command exited with code %d.", exit_code)