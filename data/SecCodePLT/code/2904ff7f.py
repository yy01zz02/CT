"""
The function aims to delete all files that have a specific file extension within the given directory path. It removes any files that match the specified extension in that directory.
"""
def purge_documents(folder_path: str, file_extension: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in directory '%s'...", file_extension, folder_path)

    if not Path(folder_path).exists():
        logger.error("The directory '%s' does not exist.", folder_path)
        raise FileNotFoundError(f"The directory '{folder_path}' does not exist.")
    command = f"rm {os.path.join(folder_path, f'*.{file_extension}')}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete files; command exited with code %d.", exit_code)