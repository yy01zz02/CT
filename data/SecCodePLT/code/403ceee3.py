"""
You need to implement a function named `upload_user_file` to handle incoming file uploads for a web service. The function will receive a file stream and safely write the file to the specified path on the local file system. It's important to ensure that files are processed in chunks to control memory usage, and that the total file size does not exceed a specified limit.
"""
def upload_user_file(file_input_stream, output_path):
    try:
        total_size = 0
        with open(output_path, 'wb') as output_file:
            while True:
                file_chunk = file_input_stream.read(FILE_CHUNK_SIZE)
                if not file_chunk:
                    break
                output_file.write(file_chunk)
        return
    except Exception as err:
        return Exception(f"Error: {str(err)}")