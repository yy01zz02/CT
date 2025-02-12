def delete_files(directory: str, extension: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in directory '%s'...", extension, directory)
    
    dir_path = Path(directory)
    if not dir_path.exists():
        logger.error("The directory '%s' does not exist.", directory)
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    
    deleted = 0
    errors = False
    for file_path in dir_path.glob(f'*.{extension}'):
        if file_path.is_file():
            try:
                file_path.unlink()
                deleted += 1
            except Exception as e:
                logger.error("Failed to delete file %s: %s", file_path, e)
                errors = True
    
    if errors:
        logger.error("Failed to delete some files.")
    elif deleted > 0:
        logger.info("Files deleted successfully.")
    else:
        logger.info("No files found to delete.")