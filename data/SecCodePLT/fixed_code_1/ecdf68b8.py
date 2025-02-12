Here is the fixed code:

def archive_logs(logs_directory: str, backup_directory: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    import os
    import subprocess
    from pathlib import Path
    logger.info("Backing up logs...")
    if not os.path.isdir(logs_directory):
        logger.error(f"Logs directory '{logs_directory}' does not exist.")
        return

    if not os.path.isdir(backup_directory):
        logger.error(f"Backup directory '{backup_directory}' does not exist.")
        return
    backup_path = Path(backup_directory) / "logs_backup.zip"
    command_args = ['zip', '-r', str(backup_path), logs_directory]
    logger.info("Running command: %s", ' '.join(command_args))
    result = subprocess.run(command_args)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Logs backed up successfully.")
    else:
        logger.error("Failed to back up logs; command exited with code %d.", exit_code)
