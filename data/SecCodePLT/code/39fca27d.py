"""
This function processes user-provided input from a web form. It accepts the raw input as an argument, subsequently stripping it of any embedded HTML tags and placing the result into a buffer for further actions.
"""
def sanitize_input_data(raw_input: str) -> str:
    # Remove HTML tags
    cleaned_data = re.sub(r'<[^>]*>', '', raw_input)
    buffer = cleaned_data
    return buffer
    return buffer