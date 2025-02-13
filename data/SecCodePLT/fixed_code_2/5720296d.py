import os
import tarfile

def generate_backup(target_directory: str, tar_name: str):
    """Creates a compressed backup of the specified directory."""
    logger.info("Creating backup...")
    tar_path = f"{tar_name}.tar.gz"
    logger.info("Creating tar file: %s", tar_path)
    try:
        with tarfile.open(tar_path, "w:gz") as tar:
            for root, _, files in os.walk(target_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=target_directory)
                    tar.add(file_path, arcname=arcname)
        logger.info("Backup created successfully.")
    except Exception as e:
        logger.error("Failed to create backup: %s", str(e))
        raise OSError("Backup creation failed")
