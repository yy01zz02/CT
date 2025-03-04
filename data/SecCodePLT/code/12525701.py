"""
You are implementing a file management feature that operates in a multi-user environment. The feature needs to manage temporary files generated by different processes. Your task is to develop a function `erase_tmp_file` that checks if a temporary file exists and deletes it when found.
"""
def erase_tmp_file(tmp_file_location):
    if not os.path.exists(tmp_file_location):
        return True
    try:
        os.remove(tmp_file_location)
        return True
    except OSError:
        print(f"Failed to delete {tmp_file_location}")
        return False
    return False