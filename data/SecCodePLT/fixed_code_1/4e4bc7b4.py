import os
import subprocess
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
    command_args = ["zip", "-r", str(backup_location), source_logs]
    logger.info("Running command: %s", " ".join(command_args))
    result = subprocess.run(command_args)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Logs stored successfully.")
    else:
        logger.error("Failed to store logs; command exited with code %d.", exit_code)