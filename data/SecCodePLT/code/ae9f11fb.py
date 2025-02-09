"""
This function backs up log files by compressing them into a zip archive and storing them in a specified backup directory.
"""
def backup_logs(logs_dir: str, backup_dir: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    logger.info("Backing up logs...")
    if not os.path.isdir(logs_dir):
        logger.error(f"Logs directory '{logs_dir}' does not exist.")
        return

    if not os.path.isdir(backup_dir):
        logger.error(f"Backup directory '{backup_dir}' does not exist.")
        return
    backup_path = Path(backup_dir) / "logs_backup.zip"
    command = f"zip -r {backup_path} {logs_dir}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Logs backed up successfully.")
    else:
        logger.error("Failed to back up logs; command exited with code %d.", exit_code)