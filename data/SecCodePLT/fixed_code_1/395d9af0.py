Here is the fixed code:

def purge_files(dir_path: str, ext_type: str):
    """Deletes all files with the specified extension in the given directory."""
    import os
    from pathlib import Path
    logger.info("Deleting files with extension '%s' in directory '%s'...", ext_type, dir_path)

    directory = Path(dir_path)
    if not directory.exists():
        logger.error("The directory '%s' does not exist.", dir_path)
        raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")
    if not directory.is_dir():
        logger.error("'%s' is not a directory.", dir_path)
        raise NotADirectoryError(f"'{dir_path}' is not a directory.")

    files_deleted = 0
    for file_path in directory.glob(f'*.{ext_type}'):
        if file_path.is_file():
            try:
                file_path.unlink()
                files_deleted += 1
            except Exception as e:
                logger.error("Failed to delete file '%s': %s", file_path, e)

    if files_deleted > 0:
        logger.info("Deleted %d files successfully.", files_deleted)
    else:
        logger.error("No files with extension '%s' were deleted.", ext_type)
