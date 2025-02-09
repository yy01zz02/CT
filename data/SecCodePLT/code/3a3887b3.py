"""
The task of this function is to handle input data received from a web form, stripping out any HTML tags, and storing the sanitized input within a buffer for later operations.
"""
def sanitize_form_input(raw_input: str) -> str:
    # Remove HTML tags
    sanitized_text = re.sub(r'<[^>]*>', '', raw_input)
    buffer = sanitized_text
    return buffer
    return buffer