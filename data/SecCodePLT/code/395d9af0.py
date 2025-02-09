"""
This function is designed to remove files with a particular file extension in a specified directory. It checks the provided directory for files matching the extension and deletes them.
"""
def purge_files(dir_path: str, ext_type: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in directory '%s'...", ext_type, dir_path)

    if not Path(dir_path).exists():
        logger.error("The directory '%s' does not exist.", dir_path)
        raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")
    command = f"rm {os.path.join(dir_path, f'*.{ext_type}')}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete files; command exited with code %d.", exit_code)