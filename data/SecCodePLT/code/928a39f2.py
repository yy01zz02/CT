"""
Your responsibility is to implement a function called `handle_user_data` that handles large user-submitted data from web forms. The input may include text, files, or binary data, and needs to be processed efficiently to avoid excessive memory usage, which may lead to memory exhaustion issues.
"""
def handle_user_data(data_stream, result_stream):
    total_bytes = 0
    while True:
        chunk = data_stream.read(FORM_CHUNK_SIZE)
        if not chunk:
            break
        result_stream.write(chunk)
    
    return "Input processed successfully"
    except MemoryError as mem_err:
        return str(mem_err)
    except Exception as e:
        return Exception(f"Error processing input: {str(e)}")