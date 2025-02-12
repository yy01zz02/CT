def compress_logs(source_dir: str, save_dir: str):
    """Backs up log files by compressing them into a zip archive and storing them in a backup directory."""
    import os
    import zipfile
    from pathlib import Path
    logger.info("Backing up logs...")
    if not os.path.isdir(source_dir):
        logger.error(f"Logs directory '{source_dir}' does not exist.")
        return

    if not os.path.isdir(save_dir):
        logger.error(f"Backup directory '{save_dir}' does not exist.")
        return

    save_path = Path(save_dir) / "logs_backup.zip"
    try:
        with zipfile.ZipFile(save_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=source_dir)
                    zipf.write(file_path, arcname)
        logger.info("Logs backed up successfully.")
    except Exception as e:
        logger.error("Failed to back up logs: %s", str(e))