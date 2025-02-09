"""
This function generates an XML response by embedding user-provided input into a predefined XML template. The function replaces the placeholder in the template with the user content.
"""
def build_xml_reply(user_text: str) -> str:
    return xml_template.format(user_text=user_text)