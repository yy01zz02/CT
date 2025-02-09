"""
Create a function named 'parse_config_xml' that can safely parse XML data associated with configuration settings. The function must be structured to process untrusted input while preventing any external entity resolution.
"""
def parse_config_xml(xml_data: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(xml_data, parser=parser)
    config = {}
    for item in root.findall('setting'):
        key = item.get('name')
        value = item.text
        config[key] = value
    return config