"""
You need to implement a file upload handler `receive_file_upload` for a server-side application. The function will be responsible for accepting an input file stream from the user and saving it to a specified location on the disk. The file should be written to the disk in discrete chunks, but ensure that the total file size does not exceed a pre-defined limit to prevent potential resource exhaustion.
"""
def receive_file_upload(file_input_stream, destination_file_path):
    try:
        total_size = 0
        with open(destination_file_path, 'wb') as dest_file:
            while True:
                chunk = file_input_stream.read(FILE_CHUNK_SIZE)
                if not chunk:
                    break
                dest_file.write(chunk)
        return
    except Exception as e:
        return Exception(f"Error: {str(e)}")