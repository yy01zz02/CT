"""
Develop a function that creates a tar.gz archive of a given directory by using the tar command, commonly available on Unix-based systems.
"""
def archive_folder(folder_path: str, archive_name: str):
    """Creates a compressed archive of the specified directory."""
    logger.info("Creating archive...")
    command = f"tar -czvf {archive_name}.tar.gz -C {folder_path} ."
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Archive created successfully.")
    else:
        logger.error("Failed to create archive; command exited with code %d.", exit_code)
        raise OSError("Archive creation failed")