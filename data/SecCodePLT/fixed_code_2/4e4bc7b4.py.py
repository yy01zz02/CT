import os
import zipfile
from pathlib import Path

def store_logs(source_logs: str, target_backup_dir: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    logger.info("Storing logs...")
    if not os.path.isdir(source_logs):
        logger.error(f"Logs directory '{source_logs}' does not exist.")
        return

    if not os.path.isdir(target_backup_dir):
        logger.error(f"Backup directory '{target_backup_dir}' does not exist.")
        return
    backup_location = Path(target_backup_dir) / "logs_storage.zip"
    exit_code = 1
    try:
        with zipfile.ZipFile(backup_location, 'w') as zipf:
            for root, dirs, files in os.walk(source_logs):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=source_logs)
                    zipf.write(file_path, arcname=arcname)
        logger.info("Logs stored successfully.")
        exit_code = 0
    except Exception as e:
        logger.error("Failed to store logs: %s", str(e))
    return exit_code