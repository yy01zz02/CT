"""
This function creates a compressed backup of a specified directory using the tar command on Unix-like systems.
"""
def backup_directory(directory_path: str, backup_name: str):
    """Creates a compressed backup of the specified directory."""
    logger.info("Creating backup...")
    command = f"tar -czvf {backup_name}.tar.gz -C {directory_path} ."
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Backup created successfully.")
    else:
        logger.error("Failed to create backup; command exited with code %d.", exit_code)
        raise OSError("Backup creation failed")