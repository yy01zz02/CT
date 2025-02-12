def remove_files(folder: str, ext: str):
    """Deletes all files with the specified extension in the given directory."""
    import os
    from pathlib import Path
    import logging
    logger = logging.getLogger(__name__)

    logger.info("Deleting files with extension '%s' in directory '%s'...", ext, folder)

    folder_path = Path(folder)
    if not folder_path.exists() or not folder_path.is_dir():
        logger.error("The directory '%s' does not exist.", folder)
        raise FileNotFoundError(f"The directory '{folder}' does not exist.")

    deleted = 0
    for file in folder_path.glob(f'*.{ext}'):
        if file.is_file():
            try:
                file.unlink()
                logger.info("Deleted file: %s", file)
                deleted += 1
            except Exception as e:
                logger.error("Failed to delete %s: %s", file, e)

    if deleted > 0:
        logger.info("Successfully deleted %d files.", deleted)
    else:
        logger.warning("No files with extension '%s' were deleted from '%s'.", ext, folder)
