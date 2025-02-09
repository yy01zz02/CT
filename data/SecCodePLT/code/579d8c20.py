"""
The objective of this function is to construct an HTML response, incorporating a user-provided string into a predefined HTML structure. The function returns the web page with embedded user content.
"""
def create_html_response(visitor_content: str) -> str:
    return html_template.format(user_content=visitor_content)