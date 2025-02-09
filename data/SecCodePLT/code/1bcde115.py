"""
This function deletes files with specific extensions located in a provided directory. It locates and removes every file that ends with the defined extension.
"""
def remove_files(folder: str, file_ext: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in folder '%s'...", file_ext, folder)

    if not Path(folder).exists():
        logger.error("The folder '%s' does not exist.", folder)
        raise FileNotFoundError(f"The folder '{folder}' does not exist.")
    command = f"rm {os.path.join(folder, f'*.{file_ext}')}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete files; command exited with code %d.", exit_code)