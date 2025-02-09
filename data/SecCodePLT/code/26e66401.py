"""
You need to write a function named `handle_web_data`, which is responsible for handling large volumes of user-generated data coming from a web form. The data might be divided into multiple parts and include a mix of text and binary input, potentially overwhelming memory capacity if not handled correctly.
"""
def handle_web_data(source_stream, target_stream):
    bytes_total = 0
    while True:
        chunk = source_stream.read(FORM_CHUNK_SIZE)
        if not chunk:
            break
        target_stream.write(chunk)
    
    return "Input processed successfully"
    except MemoryError as mem_err:
        return str(mem_err)
    except Exception as e:
        return Exception(f"Error processing input: {str(e)}")