import os
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def remove_files(folder: str, file_ext: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in folder '%s'...", file_ext, folder)

    folder_path = Path(folder)
    if not folder_path.exists():
        logger.error("The folder '%s' does not exist.", folder)
        raise FileNotFoundError(f"The folder '{folder}' does not exist.")

    exit_code = 0
    for file_path in folder_path.glob(f'*.{file_ext}'):
        if file_path.is_file():
            try:
                file_path.unlink()
                logger.info("Deleted file: %s", file_path)
            except OSError as e:
                logger.error("Failed to delete file %s: %s", file_path, e)
                exit_code = 1

    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete one or more files.")

    return exit_code
