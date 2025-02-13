```
def create_backup(folder_path: str, archive_name: str):
    """Creates a compressed backup of the specified directory."""
    import os
    import tarfile
    logger.info("Creating backup...")
    archive_file = f"{archive_name}.tar.gz"
    original_dir = os.getcwd()
    try:
        abs_folder = os.path.abspath(folder_path)
        archive_path = os.path.abspath(archive_file)
        os.chdir(abs_folder)
        with tarfile.open(archive_path, "w:gz") as tar:
            tar.add(".")
        logger.info("Backup created successfully.")
    except Exception as e:
        logger.error("Failed to create backup: %s", e)
        raise OSError("Backup creation failed") from e
    finally:
        os.chdir(original_dir)
