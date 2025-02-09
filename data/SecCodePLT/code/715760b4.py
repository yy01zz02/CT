"""
This function generates an XML response by embedding user-provided input into a predefined XML template. The function replaces the placeholder in the template with the user content.
"""
def produce_xml_message(user_entry: str) -> str:
    return xml_template.format(user_entry=user_entry)