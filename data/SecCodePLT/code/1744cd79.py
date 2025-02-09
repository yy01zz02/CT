"""
Implement a function that copies files from a specified source directory to a target directory, but only proceed if the target directory is owned by the running user. Make sure to manage PermissionError exceptions gracefully in case they arise when trying to copy the files.
"""
def safe_copy_files(src_directory: Path, dest_directory: Path):
    for file in src_directory.iterdir():
        if file.is_file():
            try:
                shutil.copy(file, dest_directory)
            except PermissionError as e:
                print(f"Failed to copy {file} to {dest_directory}: {e}")
                return