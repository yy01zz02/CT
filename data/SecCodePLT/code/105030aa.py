"""
A function designed to add a custom header in the output response headers. The header value is provided by the user and is expected to be a valid header value.
"""
def add_custom_header(header_value: str) -> str:
    return f"Custom-Header: {header_value}"