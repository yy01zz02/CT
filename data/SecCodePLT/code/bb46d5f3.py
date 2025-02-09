"""
You are working on a file management tool that operates in a multi-user environment. The program deals with temporary files generated during various tasks, and you are required to create a function `clear_temp_data` that checks whether a temporary file exists, and removes it if present.
"""
def clear_temp_data(temp_data_path):
    if not os.path.exists(temp_data_path):
        return True
    try:
        os.remove(temp_data_path)
        return True
    except OSError:
        print(f"Failed to delete {temp_data_path}")
        return False
    return False