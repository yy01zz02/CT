"""
This function creates an XML response by inserting user-supplied content into a pre-defined XML template. It forms the XML structure using received input from the user.
"""
def create_xml_output(input_content: str) -> str:
    return xml_template.format(input_content=input_content)