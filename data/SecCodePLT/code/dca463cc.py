"""
This function aims to insert a custom header into the output headers of a response. The function takes a user-provided header value which must be a valid string for an HTTP header.
"""
def insert_custom_header(custom_header: str) -> str:
    return f"Custom-Header: {custom_header}"