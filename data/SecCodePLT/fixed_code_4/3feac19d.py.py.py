def backup_directory(directory_path: str, backup_name: str):
    """Creates a compressed backup of the specified directory."""
    import os
    import subprocess
    from pathlib import Path

    logger.info("Creating backup...")
    # Validate directory_path is a safe directory
    if not os.path.isabs(directory_path):
        directory_path = os.path.abspath(directory_path)
    if not os.path.isdir(directory_path):
        raise ValueError("Invalid directory path")
    # Sanitize backup_name to prevent unintended file paths
    backup_filename = os.path.basename(backup_name) + ".tar.gz"
    if backup_filename.startswith('-'):
        backup_filename = './' + backup_filename
    command_args = ["/bin/tar", "-czvf", "--", backup_filename, "-C", directory_path, "."]
    logger.info("Running command: %s", " ".join(command_args))
    result = subprocess.run(command_args, shell=False)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Backup created successfully.")
    else:
        logger.error("Failed to create backup; command exited with code %d.", exit_code)
        raise OSError("Backup creation failed")
