import os
import shutil
from logging import logger

def save_folder(folder_path: str, save_name: str):
    """Creates a compressed backup of the specified directory."""
    logger.info("Creating backup...")
    
    if not os.path.isdir(folder_path):
        logger.error("Invalid directory path provided: %s", folder_path)
        raise ValueError("Invalid directory path")

    safe_save_name = os.path.basename(save_name.replace("/", "").replace("\\", ""))
    
    try:
        archive_path = shutil.make_archive(safe_save_name, 'gztar', folder_path)
        logger.info("Backup created successfully at: %s", archive_path)
    except Exception as e:
        logger.error("Failed to create backup: %s", str(e))
        raise OSError("Backup creation failed") from e
