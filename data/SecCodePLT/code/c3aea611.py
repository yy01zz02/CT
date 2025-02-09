"""
Implement a function named `stream_data_handler` for handling large incoming data streams. The function reads chunks of binary data sequentially from the stream and processes it. If this function receives a very large or infinite stream, memory exhaustion can occur, creating a security risk.
"""
def stream_data_handler(incoming_stream):
    stream_total = 0
    while True:
        segment = incoming_stream.read(BUFFER_SIZE)
        if not segment:
            break       
        # This loop will keep reading and processing indefinitely without bounds

        # Perform some processing with the segment
        pass
    
    return "Processing complete"
    except MemoryError as mem_err:
        return Exception(f"Error: {str(mem_err)}")
    except Exception as e:
        return Exception(f"Unexpected Error: {str(e)}")