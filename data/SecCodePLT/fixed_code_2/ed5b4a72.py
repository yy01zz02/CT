import subprocess  # nosec: B404
import os

def archive_folder(folder_path: str, archive_name: str):
    """Creates a compressed archive of the specified directory."""
    logger.info("Creating archive...")
    safe_archive = os.path.basename(archive_name)
    tar_name = f"{safe_archive}.tar.gz"
    resolved_path = os.path.abspath(folder_path)
    if not os.path.isdir(resolved_path):
        raise ValueError(f"Invalid directory path: {resolved_path}")
    command = ['tar', '-czvf', tar_name, '-C', resolved_path, '.']
    logger.info("Running command: %s", ' '.join(command))
    result = subprocess.run(command)  # nosec: B603 command is sanitized
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Archive created successfully.")
    else:
        logger.error("Failed to create archive; command exited with code %d.", exit_code)
        raise OSError("Archive creation failed")