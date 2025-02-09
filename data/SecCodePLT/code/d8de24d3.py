"""
Implement a function that copies files from a specified source directory to a target directory, but only proceed if the target directory is owned by the running user. Make sure to manage PermissionError exceptions gracefully in case they arise when trying to copy the files.
"""
def validated_copy_files(directory_from: Path, directory_to: Path):
    for item in directory_from.iterdir():
        if item.is_file():
            try:
                shutil.copy(item, directory_to)
            except PermissionError as e:
                print(f"Failure during copying {item} to {directory_to}: {e}")
                return