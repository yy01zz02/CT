import subprocess
import os
import logging

logger = logging.getLogger(__name__)

def compress_directory(dir_path: str, compressed_name: str):
    """Creates a compressed archive of the specified directory."""
    logger.info("Creating archive...")
    output_filename = f"{compressed_name}.tar.gz"
    command = ['tar', '-czvf', output_filename, '-C', dir_path, '.']
    logger.info("Running command: %s", ' '.join(command))
    result = subprocess.run(command)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Archive created successfully.")
    else:
        logger.error("Failed to create archive; command exited with code %d.", exit_code)
        raise OSError("Archive creation failed")
