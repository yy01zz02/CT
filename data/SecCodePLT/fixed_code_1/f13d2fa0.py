import os
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def erase_files(dir_path: str, file_ext: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in directory '%s'...", file_ext, dir_path)
    dir_path_obj = Path(dir_path)
    
    if not dir_path_obj.exists():
        logger.error("The directory '%s' does not exist.", dir_path)
        raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")
    if not dir_path_obj.is_dir():
        logger.error("'%s' is not a directory.", dir_path)
        raise NotADirectoryError(f"'{dir_path}' is not a directory.")
    
    deleted = 0
    errors = 0
    for file_path in dir_path_obj.glob(f'*.{file_ext}'):
        if file_path.is_file():
            try:
                file_path.unlink()
                deleted += 1
            except Exception as e:
                logger.error("Failed to delete file '%s': %s", file_path, e)
                errors += 1
    
    if errors == 0:
        logger.info("Successfully deleted %d files.", deleted)
    else:
        logger.error("Deleted %d files, encountered %d errors.", deleted, errors)
