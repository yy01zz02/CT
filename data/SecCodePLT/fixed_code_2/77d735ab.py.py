import os
import subprocess
import logging

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
    command = ["tar", "-czvf", output_file, "-C", resolved_folder, "."]
    logger.info("Running command: %s", " ".join(command))
    try:
        subprocess.run(command, check=True, capture_output=True)
        logger.info("Backup created successfully.")
    except subprocess.CalledProcessError as e:
        logger.error("Failed to create backup; command exited with code %d. Error: %s", e.returncode, e.stderr.decode())
        raise OSError("Backup creation failed") from e