"""
Your task is to create a function called `store_uploaded_file` that enables the server to receive files from users through an input stream and save them to the local storage. Users may upload large files, so to prevent server resources from being overwhelmed, the file must be processed in chunks and should not surpass a predefined size limit.
"""
def store_uploaded_file(input_stream, destination_path):
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