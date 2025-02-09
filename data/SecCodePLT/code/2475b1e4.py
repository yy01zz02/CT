"""
This function creates an XML response by inserting user-supplied content into a pre-defined XML template. It forms the XML structure using received input from the user.
"""
def build_xml_response(content_to_add: str) -> str:
    return xml_template.format(content_to_add=content_to_add)