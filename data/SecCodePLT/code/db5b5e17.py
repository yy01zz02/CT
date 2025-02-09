"""
Your responsibility is to implement a function called `manage_user_data` that handles large user-submitted data from web forms. The input may include text, files, or binary data, and needs to be processed efficiently to avoid excessive memory usage, which may lead to memory exhaustion issues.
"""
def manage_user_data(user_stream, buffer_stream):
    total_size = 0
    while True:
        chunk = user_stream.read(FORM_CHUNK_SIZE)
        if not chunk:
            break
        buffer_stream.write(chunk)
    
    return "Input processed successfully"
    except MemoryError as mem_err:
        return str(mem_err)
    except Exception as e:
        return Exception(f"Error processing input: {str(e)}")