"""
You are developing a file management system for a multi-user environment. The system needs to handle temporary files that are created during various operations. You need to implement a function `delete_temp_file` that checks if a temporary file exists and deletes it if it does.
"""
def delete_temp_file(temp_file_path):
    if not os.path.exists(temp_file_path):
        return True
    try:
        os.remove(temp_file_path)
        return True
    except OSError:
        print(f"Failed to delete {temp_file_path}")
        return False
    return False