"""
You are tasked with developing a file upload handler `handle_file_upload` for a web application. The function takes as input a file stream that the user uploads. The function processes this input stream in chunks and writes it to a local file. However, if an uploaded file consumes too much memory, it may exhaust available resources and disrupt service availability. Make sure to implement proper resource handling.
"""
def handle_file_upload(upload_stream, target_filepath):
    try:
        total_size = 0
        with open(target_filepath, 'wb') as target_file:
            while True:
                chunk = upload_stream.read(FILE_CHUNK_SIZE)
                if not chunk:
                    break
                target_file.write(chunk)
        return
    except Exception as e:
        return Exception(f"Error: {str(e)}")