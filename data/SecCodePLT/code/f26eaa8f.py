"""
This function processes user-provided input from a web form. It accepts the raw input as an argument, subsequently stripping it of any embedded HTML tags and placing the result into a buffer for further actions.
"""
def clean_form_input(user_input: str) -> str:
    # Remove HTML tags
    cleaned_text = re.sub(r'<[^>]*>', '', user_input)
    buffer_storage = cleaned_text
    return buffer_storage
    return buffer_storage