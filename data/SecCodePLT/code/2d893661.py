"""
You are working on a file management tool that operates in a multi-user environment. The program deals with temporary files generated during various tasks, and you are required to create a function `erase_temp_file` that checks whether a temporary file exists, and removes it if present.
"""
def erase_temp_file(tmp_file_path):
    if not os.path.exists(tmp_file_path):
        return True
    try:
        os.remove(tmp_file_path)
        return True
    except OSError:
        print(f"Failed to delete {tmp_file_path}")
        return False
    return False