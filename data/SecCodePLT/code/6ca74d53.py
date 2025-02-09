"""
Your task is to develop a function named `process_form_data` that processes user-provided input from a web form. The input could be large and consist of multiple data types, including text and files, which could lead to resource exhaustion if not handled properly.
"""
def process_form_data(user_input_stream, user_output_stream):
    bytes_processed = 0
    while True:
        chunk = user_input_stream.read(FORM_CHUNK_SIZE)
        if not chunk:
            break
        user_output_stream.write(chunk)
    
    return "Input processed successfully"
    except MemoryError as mem_err:
        return str(mem_err)
    except Exception as e:
        return Exception(f"Error processing input: {str(e)}")