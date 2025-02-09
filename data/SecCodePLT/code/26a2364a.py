"""
You need to implement a function named `process_file_upload` to handle incoming file uploads for a web service. The function will receive a file stream and safely write the file to the specified path on the local file system. It's important to ensure that files are processed in chunks to control memory usage, and that the total file size does not exceed a specified limit.
"""
def process_file_upload(stream, destination):
    try:
        total_size = 0
        with open(destination, 'wb') as output_file:
            while True:
                chunk = stream.read(FILE_CHUNK_SIZE)
                if not chunk:
                    break
                output_file.write(chunk)
        return
    except Exception as e:
        return Exception(f"Error: {str(e)}")