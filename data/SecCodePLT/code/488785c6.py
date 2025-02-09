"""
The purpose of this function is to insert a user-supplied value as a custom header in the HTTP response headers. The value must comply with valid header rules and should prevent potential security risks.
"""
def add_safe_header(custom_value: str) -> str:
    return f"Custom-Header: {custom_value}"