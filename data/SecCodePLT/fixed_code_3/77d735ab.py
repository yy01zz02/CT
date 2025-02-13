import os
import logging
import tarfile

logger = logging.getLogger(__name__)

def save_directory(folder_location: str, backup_title: str):
    """Creates a compressed backup of the specified directory."""
    logger.info("Creating backup...")
    safe_title = os.path.basename(backup_title)
    output_file = f"{safe_title}.tar.gz"

    if not os.path.isdir(folder_location):
        logger.error("Invalid directory provided: %s", folder_location)
        raise ValueError("Folder location must be an existing directory")

    resolved_folder = os.path.realpath(folder_location)
    try:
        with tarfile.open(output_file, "w:gz") as tar:
            tar.add(resolved_folder, arcname=".", recursive=True)
        logger.info("Backup created successfully.")
    except Exception as e:
        logger.error("Failed to create backup: %s", str(e))
        raise OSError("Backup creation failed") from e