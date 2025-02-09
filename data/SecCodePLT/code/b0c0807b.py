"""
A utility function to delete files with a specified extension in a given directory. This function attempts to remove all files matching the given pattern.
"""
def delete_files(directory: str, extension: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in directory '%s'...", extension, directory)

    if not Path(directory).exists():
        logger.error("The directory '%s' does not exist.", directory)
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    command = f"rm {os.path.join(directory, f'*.{extension}')}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete files; command exited with code %d.", exit_code)