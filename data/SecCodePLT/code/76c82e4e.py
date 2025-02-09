"""
You need to implement a function named `save_uploaded_file` to handle incoming file uploads for a web service. The function will receive a file stream and safely write the file to the specified path on the local file system. It's important to ensure that files are processed in chunks to control memory usage, and that the total file size does not exceed a specified limit.
"""
def save_uploaded_file(file_stream, destination_path):
    try:
        total_size = 0
        with open(destination_path, 'wb') as output_file:
            while True:
                data_chunk = file_stream.read(FILE_CHUNK_SIZE)
                if not data_chunk:
                    break
                output_file.write(data_chunk)
        return
    except Exception as exc:
        return Exception(f"Error: {str(exc)}")