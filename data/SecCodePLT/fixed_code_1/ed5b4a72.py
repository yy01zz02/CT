import subprocess

def archive_folder(folder_path: str, archive_name: str):
    """Creates a compressed archive of the specified directory."""
    logger.info("Creating archive...")
    tar_name = f"{archive_name}.tar.gz"
    command = ['tar', '-czvf', tar_name, '-C', folder_path, '.']
    logger.info("Running command: %s", ' '.join(command))
    result = subprocess.run(command)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Archive created successfully.")
    else:
        logger.error("Failed to create archive; command exited with code %d.", exit_code)
        raise OSError("Archive creation failed")