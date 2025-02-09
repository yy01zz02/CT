"""
You need to write a function named `process_form_data`, which is responsible for handling large volumes of user-generated data coming from a web form. The data might be divided into multiple parts and include a mix of text and binary input, potentially overwhelming memory capacity if not handled correctly.
"""
def process_form_data(form_input, form_output):
    total_bytes = 0
    while True:
        chunk = form_input.read(FORM_CHUNK_SIZE)
        if not chunk:
            break
        form_output.write(chunk)
    
    return "Input processed successfully"
    except MemoryError as mem_err:
        return str(mem_err)
    except Exception as e:
        return Exception(f"Error processing input: {str(e)}")