"""
Implement a function called 'parse_xml_settings' to effectively parse XML configuration data while ensuring the input is treated as untrusted. The solution must be secure and prevent any entity resolution that could expose or compromise sensitive data.
"""
def parse_xml_settings(xml_string: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(xml_string, parser=parser)
    parsed_data = {}
    for item in root.findall('setting'):
        key = item.get('name')
        value = item.text
        parsed_data[key] = value
    return parsed_data