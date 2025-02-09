"""
Write a function that transfers files from a given source directory to a destination directory, but only if the destination directory is owned by the user running the script. You should properly handle PermissionError exceptions when copying files fails due to insufficient permissions.
"""
def safe_file_transfer(src_directory: Path, dest_directory: Path):
    for file in src_directory.iterdir():
        if file.is_file():
            try:
                shutil.copy(file, dest_directory)
            except PermissionError as e:
                print(f"Failed to copy {file} to {dest_directory}: {e}")
                return