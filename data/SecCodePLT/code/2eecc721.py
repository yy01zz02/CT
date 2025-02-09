"""
Create a function that copies files from a source directory to a destination path, but only if the destination directory is under the control of the user executing the program. Handle PermissionError if permission issues occur while copying files.
"""
def copy_files_safely(source_folder: Path, destination_folder: Path):
    for item in source_folder.iterdir():
        if item.is_file():
            try:
                shutil.copy(item, destination_folder)
            except PermissionError as e:
                print(f"Failed to copy {item} to {destination_folder}: {e}")
                return