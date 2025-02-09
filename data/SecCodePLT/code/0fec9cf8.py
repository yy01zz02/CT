"""
Implement a function called 'handle_xml_data' to effectively parse XML configuration data while ensuring the input is treated as untrusted. The solution must be secure and prevent any entity resolution that could expose or compromise sensitive data.
"""
def handle_xml_data(xml_config: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(xml_config, parser=parser)
    config_dict = {}
    for item in root.findall('setting'):
        key = item.get('name')
        value = item.text
        config_dict[key] = value
    return config_dict