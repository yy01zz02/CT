import os
import zipfile
from pathlib import Path

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
    try:
        with zipfile.ZipFile(target_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            base_dir = os.path.dirname(logs_directory)
            for root, _, files in os.walk(logs_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, base_dir)
                    zipf.write(file_path, arcname=arcname)
        logger.info("Logs compressed successfully.")
    except Exception as e:
        logger.error(f"Failed to compress logs: {e}")