"""
The function aims to delete all files that have a specific file extension within the given directory path. It removes any files that match the specified extension in that directory.
"""
def remove_files(folder: str, file_type: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in directory '%s'...", file_type, folder)

    if not Path(folder).exists():
        logger.error("The folder '%s' does not exist.", folder)
        raise FileNotFoundError(f"The folder '{folder}' does not exist.")
    command = f"rm {os.path.join(folder, f'*.{file_type}')}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete files; command exited with code %d.", exit_code)