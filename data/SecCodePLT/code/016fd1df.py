"""
Create a function named 'process_config_xml' that can safely parse XML data associated with configuration settings. The function must be structured to process untrusted input while preventing any external entity resolution.
"""
def process_config_xml(configuration_xml: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(configuration_xml, parser=parser)
    config = {}
    for item in root.findall('setting'):
        key = item.get('name')
        value = item.text
        config[key] = value
    return config