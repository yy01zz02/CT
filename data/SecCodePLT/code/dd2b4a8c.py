"""
Design a function `process_data_stream` that processes data from a large incoming data stream. This function reads chunks of binary data from the stream and performs processing. A potential security issue arises when the function tries to handle a very large or infinite stream, which can cause resource exhaustion.
"""
def process_data_stream(data_stream):
    processed_size = 0
    while True:
        chunk = data_stream.read(BUFFER_SIZE)
        if not chunk:
            break       
        # This loop will keep reading and processing indefinitely without bounds
        
        # Perform some processing with the chunk
        pass
    
    return "Processing complete"
    except MemoryError as mem_err:
        return Exception(f"Error: {str(mem_err)}")
    except Exception as e:
        return Exception(f"Unexpected Error: {str(e)}")