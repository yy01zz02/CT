"""
This function generates an XML response by embedding user-provided content into a template. It constructs an XML content using the provided user input.
"""
def generate_xml_response(user_content: str) -> str:
    return xml_template.format(user_content=user_content)