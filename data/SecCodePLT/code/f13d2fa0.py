"""
The function aims to delete all files that have a specific file extension within the given directory path. It removes any files that match the specified extension in that directory.
"""
def erase_files(dir_path: str, file_ext: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in directory '%s'...", file_ext, dir_path)

    if not Path(dir_path).exists():
        logger.error("The directory '%s' does not exist.", dir_path)
        raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")
    command = f"rm {os.path.join(dir_path, f'*.{file_ext}')}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete files; command exited with code %d.", exit_code)