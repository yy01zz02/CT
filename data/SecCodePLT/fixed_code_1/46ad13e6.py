import os
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def erase_files(folder_path: str, file_type: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in folder '%s'...", file_type, folder_path)
    
    folder = Path(folder_path)
    if not folder.exists():
        logger.error("The folder '%s' does not exist.", folder_path)
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
    if not folder.is_dir():
        logger.error("'%s' is not a directory.", folder_path)
        raise NotADirectoryError(f"'{folder_path}' is not a directory.")
    
    success = True
    for file_path in folder.glob(f'*.{file_type}'):
        try:
            file_path.unlink()
        except OSError as e:
            logger.error("Failed to delete file '%s': %s", file_path, e)
            success = False
    
    if success:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Some files could not be deleted.")
