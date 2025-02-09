"""
This function is responsible for archiving log files from a given directory into a .zip format and saving the resulting archive in a specified backup location.
"""
def compress_logs(logs_directory: str, destination_dir: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    logger.info("Compressing logs...")
    if not os.path.isdir(logs_directory):
        logger.error(f"Logs directory '{logs_directory}' does not exist.")
        return

    if not os.path.isdir(destination_dir):
        logger.error(f"Backup directory '{destination_dir}' does not exist.")
        return
    target_path = Path(destination_dir) / "logs_backup.zip"
    command = f"zip -r {target_path} {logs_directory}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Logs compressed successfully.")
    else:
        logger.error("Failed to compress logs; command exited with code %d.", exit_code)