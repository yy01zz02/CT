import subprocess

def generate_backup(target_directory: str, tar_name: str):
    """Creates a compressed backup of the specified directory."""
    logger.info("Creating backup...")
    command = ["tar", "-czvf", f"{tar_name}.tar.gz", "-C", target_directory, "."]
    logger.info("Running command: %s", " ".join(command))
    try:
        subprocess.run(command, check=True)
        logger.info("Backup created successfully.")
    except subprocess.CalledProcessError as e:
        logger.error("Failed to create backup; command exited with code %d.", e.returncode)
        raise OSError("Backup creation failed")
