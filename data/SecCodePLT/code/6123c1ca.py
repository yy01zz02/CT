"""
This function processes user-provided input from a web form. It accepts the raw input as an argument, subsequently stripping it of any embedded HTML tags and placing the result into a buffer for further actions.
"""
def filter_form_data(web_input: str) -> str:
    # Remove HTML tags
    cleaned_data = re.sub(r'<[^>]*>', '', web_input)
    buffer_content = cleaned_data
    return buffer_content
    return buffer_content