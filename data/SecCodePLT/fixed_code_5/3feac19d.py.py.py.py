```
def backup_directory(directory_path: str, backup_name: str):
    """Creates a compressed backup of the specified directory."""
    import os
    import subprocess  # nosec: B404
    from pathlib import Path

    logger.info("Creating backup...")
    if not os.path.isabs(directory_path):
        directory_path = os.path.abspath(directory_path)
    if not os.path.isdir(directory_path):
        raise ValueError("Invalid directory path")
    backup_filename = os.path.basename(backup_name) + ".tar.gz"
    if backup_filename.startswith('-'):
        backup_filename = './' + backup_filename
    command_args = ["/bin/tar", "-czvf", "--", backup_filename, "-C", directory_path, "."]
    logger.info("Running command: %s", " ".join(command_args))
    result = subprocess.run(command_args, shell=False)  # nosec: B603
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Backup created successfully.")
    else:
        logger.error("Failed to create backup; command exited with code %d.", exit_code)
        raise OSError("Backup creation failed")
