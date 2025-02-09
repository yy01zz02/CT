"""
The goal of this function is to create an HTML response by inserting user content into a given HTML structure. The generated response will display user-provided information within a predefined format.
"""
def create_html_output(input_text: str) -> str:
    return html_template.format(user_content=input_text)