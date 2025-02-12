def archive_logs(log_directory: str, destination_directory: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    import os
    from pathlib import Path
    import zipfile
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
    try:
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(log_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=log_directory)
                    zipf.write(file_path, arcname=arcname)
        logger.info("Logs backed up successfully.")
    except Exception as e:
        logger.error("Failed to back up logs: %s", str(e))