def backup_directory(directory_path: str, backup_name: str):
    """Creates a compressed backup of the specified directory."""
    logger.info("Creating backup...")
    command_args = ["/bin/tar", "-czvf", f"{backup_name}.tar.gz", "-C", directory_path, "."]
    logger.info("Running command: %s", " ".join(command_args))
    result = subprocess.run(command_args)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Backup created successfully.")
    else:
        logger.error("Failed to create backup; command exited with code %d.", exit_code)
        raise OSError("Backup creation failed")
