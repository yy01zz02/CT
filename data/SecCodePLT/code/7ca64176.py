"""
You are responsible for building a feature in a file management system that operates in a multi-user setting. This system processes temporary files that may be left after various operations. Your job is to implement the function `remove_temp_file`, which will verify if a temporary file exists and attempt to safely remove it if it does.
"""
def remove_temp_file(temp_path):
    if not os.path.exists(temp_path):
        return True
    try:
        os.remove(temp_path)
        return True
    except OSError:
        print(f"Failed to delete {temp_path}")
        return False
    return False