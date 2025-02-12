import subprocess
import os
from logging import logger

def save_folder(folder_path: str, save_name: str):
    """Creates a compressed backup of the specified directory."""
    logger.info("Creating backup...")
    command = [
        "tar",
        "-czvf",
        f"{save_name}.tar.gz",
        "-C",
        folder_path,
        "."
    ]
    logger.info("Running command: %s", " ".join(command))
    result = subprocess.run(command)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Backup created successfully.")
    else:
        logger.error("Failed to create backup; command exited with code %d.", exit_code)
        raise OSError("Backup creation failed")
