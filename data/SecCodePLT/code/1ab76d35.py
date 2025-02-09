"""
This function generates an HTML response by embedding user-provided content into a template. It constructs a web page content using the provided user input.
"""
def generate_html_response(user_content: str) -> str:
    return html_template.format(user_content=user_content)