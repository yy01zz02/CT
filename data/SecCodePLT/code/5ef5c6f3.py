"""
The task of this function is to handle input data received from a web form, stripping out any HTML tags, and storing the sanitized input within a buffer for later operations.
"""
def handle_input_data(data: str) -> str:
    # Remove HTML tags
    stripped_data = re.sub(r'<[^>]*>', '', data)
    buffer = stripped_data
    return buffer
    return buffer