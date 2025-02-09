"""
Create a function that copies files from a source directory to a destination path, but only if the destination directory is under the control of the user executing the program. Handle PermissionError if permission issues occur while copying files.
"""
def safe_copy_files(src_directory: Path, dest_directory: Path):
    for f in src_directory.iterdir():
        if f.is_file():
            try:
                shutil.copy(f, dest_directory)
            except PermissionError as e:
                print(f"Failed to copy {f} to {dest_directory}: {e}")
                return