def compress_logs(source_dir: str, save_dir: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    import os
    import subprocess
    from pathlib import Path
    logger.info("Backing up logs...")
    if not os.path.isdir(source_dir):
        logger.error(f"Logs directory '{source_dir}' does not exist.")
        return

    if not os.path.isdir(save_dir):
        logger.error(f"Backup directory '{save_dir}' does not exist.")
        return
    save_path = Path(save_dir) / "logs_backup.zip"
    command = ["zip", "-r", str(save_path), str(source_dir)]
    logger.info("Running command: %s", " ".join(command))
    result = subprocess.run(command)
    if result.returncode == 0:
        logger.info("Logs backed up successfully.")
    else:
        logger.error("Failed to back up logs; command exited with code %d.", result.returncode)
