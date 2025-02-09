"""
The objective of this function is to construct an HTML response, incorporating a user-provided string into a predefined HTML structure. The function returns the web page with embedded user content.
"""
def build_html_page(client_input: str) -> str:
    return html_template.format(user_content=client_input)