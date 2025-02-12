Here's the fixed code:

def purge_documents(folder_path: str, file_extension: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in directory '%s'...", file_extension, folder_path)

    folder = Path(folder_path)
    if not folder.exists():
        logger.error("The directory '%s' does not exist.", folder_path)
        raise FileNotFoundError(f"The directory '{folder_path}' does not exist.")

    deleted = 0
    for file_path in folder.glob(f"*.{file_extension}"):
        try:
            file_path.unlink()
            deleted += 1
        except Exception as e:
            logger.error("Error deleting file %s: %s", file_path, e)

    if deleted > 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("No files were deleted.")
