Here is the fixed code:

import logging
import os
import subprocess

logger = logging.getLogger(__name__)

def archive_folder(folder_path: str, archive_name: str):
    """Creates a compressed backup of the specified directory."""
    if not os.path.isdir(folder_path):
        logger.error("Invalid folder path: '%s' is not a directory.", folder_path)
        raise ValueError("Invalid folder path")
    if os.path.dirname(archive_name):
        logger.error("Archive name '%s' contains directory components.", archive_name)
        raise ValueError("Archive name must not include directories")
    
    logger.info("Creating backup...")
    archive_path = f"{archive_name}.tar.gz"
    command = [
        "tar",
        "-czvf",
        archive_path,
        "-C",
        folder_path,
        "."
    ]
    logger.info("Running command: %s", " ".join(command))
    result = subprocess.run(command, shell=False)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Backup created successfully.")
    else:
        logger.error("Failed to create backup; command exited with code %d.", exit_code)
        raise OSError("Backup creation failed")
