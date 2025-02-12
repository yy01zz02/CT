def discard_files(dir_path: str, ext: str):
    """Deletes all files with the specified extension in the given directory."""
    import os
    from pathlib import Path
    import logging
    logger = logging.getLogger(__name__)
    
    logger.info("Deleting files with extension '%s' in directory '%s'...", ext, dir_path)

    directory = Path(dir_path)
    if not directory.exists():
        logger.error("The directory '%s' does not exist.", dir_path)
        raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")
    
    deleted = False
    for file_path in directory.glob(f'*.{ext}'):
        if file_path.is_file():
            try:
                file_path.unlink()
                deleted = True
            except Exception as e:
                logger.error("Failed to delete file %s: %s", file_path, e)
    
    if deleted:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete files; no matching files found or deletion attempts failed.")
