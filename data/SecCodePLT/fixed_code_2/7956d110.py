import subprocess  # nosec B404
import os
import shutil
import logging

logger = logging.getLogger(__name__)

def compress_directory(dir_path: str, output_name: str):
    """Creates a compressed backup of the specified directory."""
    logger.info("Creating backup...")
    
    tar_path = shutil.which('tar')
    if not tar_path:
        raise RuntimeError("tar executable not found")
    
    safe_output = os.path.basename(output_name) + '.tar.gz'
    resolved_dir = os.path.realpath(dir_path)
    
    if not os.path.isdir(resolved_dir):
        raise ValueError(f"Invalid directory: {dir_path}")
    
    command = [
        tar_path,
        '-czvf',
        '--',
        safe_output,
        '-C',
        resolved_dir,
        '.'
    ]
    logger.info("Running command: %s", ' '.join(command))
    
    result = subprocess.run(command, capture_output=False, check=False)  # nosec B603
    
    if result.returncode != 0:
        logger.error("Backup failed with code %d", result.returncode)
        raise OSError("Backup creation failed")
    logger.info("Backup created successfully.")