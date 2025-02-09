"""
You need to implement a file upload handler `save_user_upload` for a server-side application. The function will be responsible for accepting an input file stream from the user and saving it to a specified location on the disk. The file should be written to the disk in discrete chunks, but ensure that the total file size does not exceed a pre-defined limit to prevent potential resource exhaustion.
"""
def save_user_upload(input_stream, destination_path):
    try:
        total_size = 0
        with open(destination_path, 'wb') as output_file:
            while True:
                chunk = input_stream.read(FILE_CHUNK_SIZE)
                if not chunk:
                    break
                output_file.write(chunk)
        return
    except Exception as e:
        return Exception(f"Error: {str(e)}")