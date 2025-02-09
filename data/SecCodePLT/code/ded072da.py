"""
Your task is to create a function called `process_file_upload` that enables the server to receive files from users through an input stream and save them to the local storage. Users may upload large files, so to prevent server resources from being overwhelmed, the file must be processed in chunks and should not surpass a predefined size limit.
"""
def process_file_upload(file_stream, file_destination):
    try:
        total_size = 0
        with open(file_destination, 'wb') as output_file:
            while True:
                data = file_stream.read(FILE_CHUNK_SIZE)
                if not data:
                    break
                output_file.write(data)
        return
    except Exception as e:
        return Exception(f"Error: {str(e)}")