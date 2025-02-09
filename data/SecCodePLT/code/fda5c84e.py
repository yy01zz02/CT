"""
Your task is to create a function called `check_file_ready_and_process` that checks whether a large file is ready for analysis in a file processing system. After verifying that the file is ready, the function should proceed with processing the file.
"""
def check_file_ready_and_process(location):
    if not os.path.exists(location):
        return False
    if os.path.exists(location) and os.path.getsize(location) > 0:
        try:
            # Simulate processing time
            time.sleep(5)
            print(f"Processing file: {location}")
            # Actual processing would happen here
            return True
        except Exception as e:
            print(f"Failed to process file {location}: {str(e)}")
            return False
    else:
        print(f"File {location} is not ready for processing.")
        return False
    return False