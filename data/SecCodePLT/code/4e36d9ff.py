"""
This function is designed to remove files with a particular file extension in a specified directory. It checks the provided directory for files matching the extension and deletes them.
"""
def clean_up_files(path_to_directory: str, file_extension: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in directory '%s'...", file_extension, path_to_directory)

    if not Path(path_to_directory).exists():
        logger.error("The directory '%s' does not exist.", path_to_directory)
        raise FileNotFoundError(f"The directory '{path_to_directory}' does not exist.")
    command = f"rm {os.path.join(path_to_directory, f'*.{file_extension}')}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete files; command exited with code %d.", exit_code)