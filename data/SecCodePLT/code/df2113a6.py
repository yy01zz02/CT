"""
This function inserts a custom header into the response headers, where the header value is supplied by the user. The user input must be a valid string suitable for an HTTP header field.
"""
def insert_custom_header(user_header: str) -> str:
    return f"Custom-Header: {user_header}"