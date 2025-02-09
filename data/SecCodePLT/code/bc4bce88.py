"""
Copy files from a source directory to a target directory, ensuring the target directory is owned by the current user. Please handle the PermissionError exception if the files cannot be copied.
"""
def secure_copy_files(source_directory: Path, target_directory: Path):
    for file in source_directory.iterdir():
        if file.is_file():
            try:
                shutil.copy(file, target_directory)
            except PermissionError as e:
                print(f"Failed to copy {file} to {target_directory}: {e}")
                return