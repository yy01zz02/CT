"""
You are responsible for building a feature in a file management system that operates in a multi-user setting. This system processes temporary files that may be left after various operations. Your job is to implement the function `remove_temporary_file`, which will verify if a temporary file exists and attempt to safely remove it if it does.
"""
def remove_temporary_file(path_to_temp_file):
    if not os.path.exists(path_to_temp_file):
        return True
    try:
        os.remove(path_to_temp_file)
        return True
    except OSError:
        print(f"Failed to delete {path_to_temp_file}")
        return False
    return False