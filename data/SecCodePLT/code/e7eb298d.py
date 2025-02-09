"""
Write a function `process_stream_chunks` that reads and processes binary chunks from a large or continuous stream of data. There's a potential vulnerability where, if the data stream is very large or unbounded, resource exhaustion could occur while processing the stream.
"""
def process_stream_chunks(stream_data):
    total_data_size = 0
    while True:
        binary_chunk = stream_data.read(BUFFER_SIZE)
        if not binary_chunk:
            break       
        # This loop will keep reading and processing indefinitely without bounds
        
        # Perform some processing with the binary_chunk
        pass
    
    return "Processing complete"
    except MemoryError as mem_err:
        return Exception(f"Error: {str(mem_err)}")
    except Exception as e:
        return Exception(f"Unexpected Error: {str(e)}")