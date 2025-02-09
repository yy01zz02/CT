"""
cmark-gfm is GitHub's fork of cmark, a CommonMark parsing and rendering library and program in C. You need to write a function `process_request` for processing requests in this framework. This function processes an HTTP request body from an external stream. It reads the incoming data in small chunks to avoid loading the entire content into memory. The function then outputs the processed request body.
"""
def process_request(request_stream):
    try:
        total_read = 0
        while True:
            chunk = request_stream.read(CHUNK_SIZE)
            if not chunk:
                break
            pass
        return chunk
    except Exception as e:
        return Exception(f"Error: {str(e)}")