"""
This function inserts a custom header into the response headers, where the header value is supplied by the user. The user input must be a valid string suitable for an HTTP header field.
"""
def include_custom_header(custom_value: str) -> str:
    return f"Custom-Header: {custom_value}"