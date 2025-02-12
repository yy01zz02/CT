import subprocess
import os
from logging import logger

def save_folder(folder_path: str, save_name: str):
    """Creates a compressed backup of the specified directory."""
    logger.info("Creating backup...")
    
    if not os.path.isdir(folder_path):
        logger.error("Invalid directory path provided: %s", folder_path)
        raise ValueError("Invalid directory path")

    safe_save_name = os.path.basename(save_name.replace("/", "").replace("\\", ""))
    command = [
        "tar",
        "-czvf",
        f"{safe_save_name}.tar.gz",
        "-C",
        folder_path,
        "--",
        "."
    ]
    
    logger.info("Running command: %s", " ".join(command))
    try:
        result = subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        logger.error("Failed to create backup; command exited with code %d.", e.returncode)
        raise OSError("Backup creation failed") from e
    logger.info("Backup created successfully.")