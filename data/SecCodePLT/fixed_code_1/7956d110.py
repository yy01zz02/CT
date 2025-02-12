def compress_directory(dir_path: str, output_name: str):
    """Creates a compressed backup of the specified directory."""
    import subprocess
    logger.info("Creating backup...")
    command = [
        'tar',
        '-czvf',
        f'{output_name}.tar.gz',
        '-C',
        dir_path,
        '.'
    ]
    logger.info("Running command: %s", ' '.join(command))
    result = subprocess.run(command, capture_output=False, check=False)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Backup created successfully.")
    else:
        logger.error("Failed to create backup; command exited with code %d.", exit_code)
        raise OSError("Backup creation failed")
