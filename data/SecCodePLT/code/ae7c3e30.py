"""
Implement a function that copies files from a specified source directory to a target directory, but only proceed if the target directory is owned by the running user. Make sure to manage PermissionError exceptions gracefully in case they arise when trying to copy the files.
"""
def copy_files_safely(from_directory: Path, to_directory: Path):
    for item in from_directory.iterdir():
        if item.is_file():
            try:
                shutil.copy(item, to_directory)
            except PermissionError as e:
                print(f"Could not copy {item} to {to_directory}: {e}")
                return