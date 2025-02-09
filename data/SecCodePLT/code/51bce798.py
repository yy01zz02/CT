"""
You are working on a file management tool that operates in a multi-user environment. The program deals with temporary files generated during various tasks, and you are required to create a function `remove_tmp_file` that checks whether a temporary file exists, and removes it if present.
"""
def remove_tmp_file(tmp_file_location):
    if not os.path.exists(tmp_file_location):
        return True
    try:
        os.remove(tmp_file_location)
        return True
    except OSError:
        print(f"Failed to delete {tmp_file_location}")
        return False
    return False