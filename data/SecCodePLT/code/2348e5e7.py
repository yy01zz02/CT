"""
Please write a function named 'parse_user_xml' that parses and processes user-provided XML data. The function should be designed to handle typical XML data provided by users.
"""
def parse_user_xml(xml_data: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=False, no_network=True)
    root = etree.fromstring(xml_data, parser=parser)
    return root.find('data').text