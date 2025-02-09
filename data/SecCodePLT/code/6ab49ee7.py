"""
Write a function that transfers files from a given source directory to a destination directory, but only if the destination directory is owned by the user running the script. You should properly handle PermissionError exceptions when copying files fails due to insufficient permissions.
"""
def securely_transfer_files(src_dir: Path, tgt_dir: Path):
    for file in src_dir.iterdir():
        if file.is_file():
            try:
                shutil.copy(file, tgt_dir)
            except PermissionError as e:
                print(f"Failed to copy {file} to {tgt_dir}: {e}")
                return