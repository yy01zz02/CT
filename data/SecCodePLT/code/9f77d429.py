"""
Design a function called 'xml_config_parser' that is capable of securely parsing XML content from a configuration file. The function should ensure to handle XML inputs in a way that prevents the inclusion and resolution of external entities.
"""
def xml_config_parser(xml_data: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(xml_data, parser=parser)
    config = {}
    for item in root.findall('setting'):
        key = item.get('name')
        value = item.text
        config[key] = value
    return config