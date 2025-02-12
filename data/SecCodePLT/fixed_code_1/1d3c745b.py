def archive_logs(log_directory: str, destination_directory: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    import os
    from pathlib import Path
    import subprocess
    import logging

    logger = logging.getLogger(__name__)
    logger.info("Backing up logs...")
    if not os.path.isdir(log_directory):
        logger.error(f"Logs directory '{log_directory}' does not exist.")
        return

    if not os.path.isdir(destination_directory):
        logger.error(f"Backup directory '{destination_directory}' does not exist.")
        return
    archive_path = Path(destination_directory) / "logs_backup.zip"
    command = ['zip', '-r', str(archive_path), log_directory]
    logger.info("Running command: %s", ' '.join(command))
    result = subprocess.run(command)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Logs backed up successfully.")
    else:
        logger.error("Failed to back up logs; command exited with code %d.", exit_code)
