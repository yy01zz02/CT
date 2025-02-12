import shutil
import os
import logging

logger = logging.getLogger(__name__)

def compress_directory(dir_path: str, compressed_name: str):
    """Creates a compressed archive of the specified directory."""
    logger.info("Creating archive...")
    if not os.path.isdir(dir_path):
        raise ValueError(f"Directory {dir_path} does not exist.")
    if os.path.dirname(compressed_name) != '':
        raise ValueError("Compressed name must not contain directory separators.")
    try:
        shutil.make_archive(compressed_name, 'gztar', dir_path)
        logger.info("Archive created successfully.")
    except Exception as e:
        logger.error("Failed to create archive: %s", e)
        raise OSError("Archive creation failed") from e
