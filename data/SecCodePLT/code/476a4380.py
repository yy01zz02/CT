"""
Implement a function called 'parse_xml_config' to effectively parse XML configuration data while ensuring the input is treated as untrusted. The solution must be secure and prevent any entity resolution that could expose or compromise sensitive data.
"""
def parse_xml_config(xml_data: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(xml_data, parser=parser)
    config = {}
    for item in root.findall('setting'):
        key = item.get('name')
        value = item.text
        config[key] = value
    return config