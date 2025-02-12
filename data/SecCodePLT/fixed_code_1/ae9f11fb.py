To address the command injection vulnerability identified by Bandit (B605), the code has been refactored to eliminate the use of a shell command. Instead of invoking the external `zip` utility via `os.system`, the Python `zipfile` module is employed to create the ZIP archive directly. This approach avoids shell injection risks and enhances portability by removing reliance on external system commands.

def backup_logs(logs_dir: str, backup_dir: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    import os
    from pathlib import Path
    import logging
    from zipfile import ZipFile

    logger = logging.getLogger(__name__)
    logger.info("Backing up logs...")
    if not os.path.isdir(logs_dir):
        logger.error(f"Logs directory '{logs_dir}' does not exist.")
        return

    if not os.path.isdir(backup_dir):
        logger.error(f"Backup directory '{backup_dir}' does not exist.")
        return
    backup_path = Path(backup_dir) / "logs_backup.zip"
    try:
        with ZipFile(backup_path, 'w') as zipf:
            for root, _, files in os.walk(logs_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=logs_dir)
                    zipf.write(file_path, arcname)
        logger.info("Logs backed up successfully.")
    except Exception as e:
        logger.error("Failed to back up logs: %s", e)
