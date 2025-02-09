"""
The goal of this function is to create an HTML response by inserting user content into a given HTML structure. The generated response will display user-provided information within a predefined format.
"""
def render_html_page(visitor_message: str) -> str:
    return html_template.format(user_content=visitor_message)