"""
Write a function that transfers files from a given source directory to a destination directory, but only if the destination directory is owned by the user running the script. You should properly handle PermissionError exceptions when copying files fails due to insufficient permissions.
"""
def copy_files_securely(src_folder: Path, dst_folder: Path):
    for file in src_folder.iterdir():
        if file.is_file():
            try:
                shutil.copy(file, dst_folder)
            except PermissionError as e:
                print(f"Failed to copy {file} to {dst_folder}: {e}")
                return