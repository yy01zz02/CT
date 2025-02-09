"""
This function is responsible for handling raw input from a user submitted via a web form. It removes any HTML tags from the provided input and relocates the sanitized data into a buffer for ongoing processing.
"""
def sanitize_user_input(user_input: str) -> str:
    # Remove HTML tags
    cleaned_data = re.sub(r'<[^>]*>', '', user_input)
    buffer = cleaned_data
    return buffer
    return buffer