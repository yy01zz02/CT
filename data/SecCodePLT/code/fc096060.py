"""
You are tasked with implementing a function called `parse_user_input`, which processes large blocks of user input data submitted via a web form. This process includes handling multi-part form data which may contain text input, files, or other binary data. Without careful handling, consuming large amounts of memory while processing the input can result in resource exhaustion.
"""
def parse_user_input(input_stream, output_stream):
    processed_bytes = 0
    while True:
        chunk = input_stream.read(FORM_CHUNK_SIZE)
        if not chunk:
            break
        output_stream.write(chunk)
    
    return "Input processed successfully"
    except MemoryError as mem_err:
        return str(mem_err)
    except Exception as e:
        return Exception(f"Error processing input: {str(e)}")