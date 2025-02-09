"""
This function is responsible for archiving log files from a given directory into a .zip format and saving the resulting archive in a specified backup location.
"""
def archive_logs(logs_folder: str, archive_dir: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    logger.info("Archiving logs...")
    if not os.path.isdir(logs_folder):
        logger.error(f"Logs directory '{logs_folder}' does not exist.")
        return

    if not os.path.isdir(archive_dir):
        logger.error(f"Backup directory '{archive_dir}' does not exist.")
        return
    archive_path = Path(archive_dir) / "logs_archive.zip"
    command = f"zip -r {archive_path} {logs_folder}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Logs archived successfully.")
    else:
        logger.error("Failed to archive logs; command exited with code %d.", exit_code)