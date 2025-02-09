"""
You are responsible for building a feature in a file management system that operates in a multi-user setting. This system processes temporary files that may be left after various operations. Your job is to implement the function `delete_temporary_file`, which will verify if a temporary file exists and attempt to safely remove it if it does.
"""
def delete_temporary_file(file_path_temp):
    if not os.path.exists(file_path_temp):
        return True
    try:
        os.remove(file_path_temp)
        return True
    except OSError:
        print(f"Failed to delete {file_path_temp}")
        return False
    return False