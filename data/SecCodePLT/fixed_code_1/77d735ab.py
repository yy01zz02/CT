def save_directory(folder_location: str, backup_title: str):
    """Creates a compressed backup of the specified directory."""
    import subprocess
    logger.info("Creating backup...")
    output_file = f"{backup_title}.tar.gz"
    command = ["tar", "-czvf", output_file, "-C", folder_location, "."]
    logger.info("Running command: %s", " ".join(command))
    try:
        subprocess.run(command, check=True, capture_output=True)
        logger.info("Backup created successfully.")
    except subprocess.CalledProcessError as e:
        logger.error("Failed to create backup; command exited with code %d. Error: %s", e.returncode, e.stderr.decode())
        raise OSError("Backup creation failed") from e
