"""
Implements a logging backup feature that compresses log files from a designated directory into a zip file and saves it in a specified backup location.
"""
def save_logs(log_folder: str, output_folder: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    logger.info("Backing up logs...")
    if not os.path.isdir(log_folder):
        logger.error(f"Logs directory '{log_folder}' does not exist.")
        return

    if not os.path.isdir(output_folder):
        logger.error(f"Backup directory '{output_folder}' does not exist.")
        return
    archive_file = Path(output_folder) / "logs_backup.zip"
    zip_command = f"zip -r {archive_file} {log_folder}"
    logger.info("Running command: %s", zip_command)
    exit_code = os.system(zip_command)
    if exit_code == 0:
        logger.info("Logs backed up successfully.")
    else:
        logger.error("Failed to back up logs; command exited with code %d.", exit_code)