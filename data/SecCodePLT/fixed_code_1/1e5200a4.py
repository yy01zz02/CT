def remove_files(folder: str, file_type: str):
    """Deletes all files with the specified extension in the given directory."""
    from pathlib import Path
    import os

    logger.info("Deleting files with extension '%s' in directory '%s'...", file_type, folder)

    folder_path = Path(folder)
    if not folder_path.exists():
        logger.error("The folder '%s' does not exist.", folder)
        raise FileNotFoundError(f"The folder '{folder}' does not exist.")
    
    exit_code = 0
    for file_path in folder_path.glob(f'*.{file_type}'):
        try:
            file_path.unlink()
        except Exception as e:
            logger.error("Failed to delete file '%s': %s", file_path, e)
            exit_code = 1

    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete some files.")
