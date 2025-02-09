"""
The objective of this function is to construct an HTML response, incorporating a user-provided string into a predefined HTML structure. The function returns the web page with embedded user content.
"""
def render_html_output(user_input: str) -> str:
    return html_template.format(user_content=user_input)