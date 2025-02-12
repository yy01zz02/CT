def create_backup(folder_path: str, archive_name: str):
    """Creates a compressed backup of the specified directory."""
    import subprocess
    logger.info("Creating backup...")
    archive_file = f"{archive_name}.tar.gz"
    try:
        exit_code = subprocess.run(
            ["/bin/tar", "-czvf", "--", archive_file, "-C", folder_path, "."],
            check=True,
        ).returncode
        logger.info("Backup created successfully.")
    except subprocess.CalledProcessError as e:
        logger.error("Failed to create backup; command exited with code %d.", e.returncode)
        raise OSError("Backup creation failed") from e