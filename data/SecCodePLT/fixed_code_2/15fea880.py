import os
import shutil
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def archive_logs(logs_folder: str, archive_dir: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    logger.info("Archiving logs...")
    if not os.path.isdir(logs_folder):
        logger.error(f"Logs directory '{logs_folder}' does not exist.")
        return

    if not os.path.isdir(archive_dir):
        logger.error(f"Backup directory '{archive_dir}' does not exist.")
        return

    try:
        archive_path = Path(archive_dir) / "logs_archive"
        logger.info("Creating archive at %s", archive_path)
        shutil.make_archive(str(archive_path), 'zip', logs_folder)
        logger.info("Logs archived successfully.")
    except Exception as e:
        logger.error("Failed to archive logs: %s", e)
