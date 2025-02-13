def archive_directory(dir_path: str, output_name: str):
    """Creates a compressed backup of the specified directory."""
    import subprocess  # nosec: B404
    import os
    logger.info("Creating backup...")
    
    if not os.path.isabs(dir_path):
        dir_path = os.path.abspath(dir_path)
    if not os.path.isdir(dir_path):
        raise ValueError(f"Invalid directory path: {dir_path}")
    
    safe_output = os.path.basename(output_name)
    command = ["tar", "-czvf", f"{safe_output}.tar.gz", "-C", dir_path, "."]
    logger.info("Running command: %s", " ".join(command))
    
    result = subprocess.run(command, capture_output=True, text=True)  # nosec: B603
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Backup created successfully.")
    else:
        logger.error("Failed to create backup; command exited with code %d.", exit_code)
        logger.error("Command stderr: %s", result.stderr)
        raise OSError("Backup creation failed")