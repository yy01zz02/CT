import os
import subprocess
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
    logger.info("Running zip command on directory: %s", logs_directory)
    try:
        result = subprocess.run(
            ['zip', '-r', str(target_path), logs_directory],
            check=True
        )
        logger.info("Logs compressed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error("Failed to compress logs; command exited with code %d.", e.returncode)
