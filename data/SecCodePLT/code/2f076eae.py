"""
This function aims to insert a custom header into the output headers of a response. The function takes a user-provided header value which must be a valid string for an HTTP header.
"""
def add_response_header(response_header: str) -> str:
    return f"Custom-Header: {response_header}"