"""
This function is responsible for handling raw input from a user submitted via a web form. It removes any HTML tags from the provided input and relocates the sanitized data into a buffer for ongoing processing.
"""
def cleanse_form_data(form_data: str) -> str:
    # Remove HTML tags
    cleaned_data = re.sub(r'<[^>]*>', '', form_data)
    buffer = cleaned_data
    return buffer
    return buffer