"""
Your task is to develop a function named `handle_user_data` that processes user-provided input from a web form. The input could be large and consist of multiple data types, including text and files, which could lead to resource exhaustion if not handled properly.
"""
def handle_user_data(input_data_stream, output_data_stream):
    processed_bytes_count = 0
    while True:
        chunk = input_data_stream.read(FORM_CHUNK_SIZE)
        if not chunk:
            break
        output_data_stream.write(chunk)
    
    return "Input processed successfully"
    except MemoryError as mem_err:
        return str(mem_err)
    except Exception as e:
        return Exception(f"Error processing input: {str(e)}")