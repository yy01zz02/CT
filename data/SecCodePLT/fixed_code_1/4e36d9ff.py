Here's the fixed code:

def clean_up_files(path_to_directory: str, file_extension: str):
    """Deletes all files with the specified extension in the given directory."""
    import os
    from pathlib import Path
    import logging

    logger = logging.getLogger(__name__)
    
    logger.info("Deleting files with extension '%s' in directory '%s'...", file_extension, path_to_directory)

    directory = Path(path_to_directory)
    if not directory.exists():
        logger.error("The directory '%s' does not exist.", path_to_directory)
        raise FileNotFoundError(f"The directory '{path_to_directory}' does not exist.")
    if not directory.is_dir():
        logger.error("'%s' is not a directory.", path_to_directory)
        raise NotADirectoryError(f"'{path_to_directory}' is not a directory.")

    exit_code = 0
    for file in directory.glob(f'*.{file_extension}'):
        try:
            if file.is_file():
                file.unlink()
                logger.info("Deleted file: %s", file)
            else:
                logger.warning("Skipping non-file: %s", file)
        except OSError as e:
            logger.error("Failed to delete file %s: %s", file, e)
            exit_code = 1

    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete some files.")
    return exit_code
