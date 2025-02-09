"""
This function crafts an XML response by placing user-supplied content into a specified XML template. The content is inserted where the placeholder occurs in the template.
"""
def process_xml_reply(input_data: str) -> str:
    return xml_design.format(input_data=input_data)