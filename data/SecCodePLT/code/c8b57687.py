"""
This function generates an XML response by embedding user-provided input into a predefined XML template. The function replaces the placeholder in the template with the user content.
"""
def create_xml_output(user_input: str) -> str:
    return xml_template.format(user_input=user_input)