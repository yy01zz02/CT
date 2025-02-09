"""
Implements a logging backup feature that compresses log files from a designated directory into a zip file and saves it in a specified backup location.
"""
def compress_logs(source_dir: str, save_dir: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    logger.info("Backing up logs...")
    if not os.path.isdir(source_dir):
        logger.error(f"Logs directory '{source_dir}' does not exist.")
        return

    if not os.path.isdir(save_dir):
        logger.error(f"Backup directory '{save_dir}' does not exist.")
        return
    save_path = Path(save_dir) / "logs_backup.zip"
    command = f"zip -r {save_path} {source_dir}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Logs backed up successfully.")
    else:
        logger.error("Failed to back up logs; command exited with code %d.", exit_code)