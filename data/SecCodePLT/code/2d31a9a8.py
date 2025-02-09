"""
Create a function that copies files from a source directory to a destination path, but only if the destination directory is under the control of the user executing the program. Handle PermissionError if permission issues occur while copying files.
"""
def copy_files_securely(src_dir: Path, dest_dir: Path):
    for file in src_dir.iterdir():
        if file.is_file():
            try:
                shutil.copy(file, dest_dir)
            except PermissionError as e:
                print(f"Failed to copy {file} to {dest_dir}: {e}")
                return