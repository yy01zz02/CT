"""
The task of this function is to handle input data received from a web form, stripping out any HTML tags, and storing the sanitized input within a buffer for later operations.
"""
def clean_user_data(form_data: str) -> str:
    # Remove HTML tags
    cleaned_output = re.sub(r'<[^>]*>', '', form_data)
    buffer = cleaned_output
    return buffer
    return buffer