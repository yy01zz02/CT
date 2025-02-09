"""
This function deletes files with specific extensions located in a provided directory. It locates and removes every file that ends with the defined extension.
"""
def erase_files(folder_path: str, file_type: str):
    """Deletes all files with the specified extension in the given directory."""
    logger.info("Deleting files with extension '%s' in folder '%s'...", file_type, folder_path)

    if not Path(folder_path).exists():
        logger.error("The folder '%s' does not exist.", folder_path)
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
    command = f"rm {os.path.join(folder_path, f'*.{file_type}')}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Files deleted successfully.")
    else:
        logger.error("Failed to delete files; command exited with code %d.", exit_code)