"""
This function processes user input from a web form. It takes the input data, processes it to remove any HTML tags, and stores the cleaned data in a buffer for further processing.
"""
def process_user_input(input_data: str) -> str:
    # Remove HTML tags
    cleaned_data = re.sub(r'<[^>]*>', '', input_data)
    buffer = cleaned_data
    return buffer
    return buffer