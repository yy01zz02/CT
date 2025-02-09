"""
This function is designed to remove files with a particular file extension in a specified directory. It checks the provided directory for files matching the extension and deletes them.
"""
def remove_files(folder: str, ext: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in directory '%s'...", ext, folder)

    if not Path(folder).exists():
        logger.error("The directory '%s' does not exist.", folder)
        raise FileNotFoundError(f"The directory '{folder}' does not exist.")
    command = f"rm {os.path.join(folder, f'*.{ext}')}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete files; command exited with code %d.", exit_code)