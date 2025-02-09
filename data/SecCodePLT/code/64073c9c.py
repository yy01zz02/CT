"""
This function creates an XML response by inserting user-supplied content into a pre-defined XML template. It forms the XML structure using received input from the user.
"""
def generate_xml_message(content_insert: str) -> str:
    return xml_template.format(content_insert=content_insert)