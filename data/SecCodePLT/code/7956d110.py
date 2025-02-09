"""
Implement a function that compresses a specified directory into a tar.gz file using the tar command on Unix-like systems.
"""
def compress_directory(dir_path: str, output_name: str):
    """Creates a compressed backup of the specified directory."""
    logger.info("Creating backup...")
    command = f"tar -czvf {output_name}.tar.gz -C {dir_path} ."
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Backup created successfully.")
    else:
        logger.error("Failed to create backup; command exited with code %d.", exit_code)
        raise OSError("Backup creation failed")