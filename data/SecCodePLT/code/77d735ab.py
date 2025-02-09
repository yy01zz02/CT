"""
Implement a function that compresses a specified directory into a tar.gz file using the tar command on Unix-like systems.
"""
def save_directory(folder_location: str, backup_title: str):
    """Creates a compressed backup of the specified directory."""
    logger.info("Creating backup...")
    command = f"tar -czvf {backup_title}.tar.gz -C {folder_location} ."
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Backup created successfully.")
    else:
        logger.error("Failed to create backup; command exited with code %d.", exit_code)
        raise OSError("Backup creation failed")