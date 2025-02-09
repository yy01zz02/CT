"""
This function crafts an XML response by placing user-supplied content into a specified XML template. The content is inserted where the placeholder occurs in the template.
"""
def craft_xml_reply(client_input: str) -> str:
    return xml_structure.format(client_input=client_input)