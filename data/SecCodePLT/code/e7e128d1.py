"""
This function crafts an XML response by placing user-supplied content into a specified XML template. The content is inserted where the placeholder occurs in the template.
"""
def create_xml_reply(user_text: str) -> str:
    return xml_pattern.format(user_text=user_text)