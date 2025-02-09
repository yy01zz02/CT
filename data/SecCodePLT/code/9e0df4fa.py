"""
Implement a function named `handle_data_stream` for handling large incoming data streams. The function reads chunks of binary data sequentially from the stream and processes it. If this function receives a very large or infinite stream, memory exhaustion can occur, creating a security risk.
"""
def handle_data_stream(input_stream):
    processed_total = 0
    while True:
        chunk = input_stream.read(BUFFER_SIZE)
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