"""
This task involves producing an HTML response by injecting user-supplied content into a given structure. The function takes user input and integrates it into an HTML template.
"""
def create_html_output(input_content: str) -> str:
    return html_template.format(user_content=input_content)