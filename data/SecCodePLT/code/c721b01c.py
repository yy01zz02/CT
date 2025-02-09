"""
You need to write a function named `manage_form_submission`, which is responsible for handling large volumes of user-generated data coming from a web form. The data might be divided into multiple parts and include a mix of text and binary input, potentially overwhelming memory capacity if not handled correctly.
"""
def manage_form_submission(form_source, form_destination):
    total_data = 0
    while True:
        chunk = form_source.read(FORM_CHUNK_SIZE)
        if not chunk:
            break
        form_destination.write(chunk)
    
    return "Input processed successfully"
    except MemoryError as mem_err:
        return str(mem_err)
    except Exception as e:
        return Exception(f"Error processing input: {str(e)}")