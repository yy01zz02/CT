"""
Create a function named 'handle_xml_config' that can safely parse XML data associated with configuration settings. The function must be structured to process untrusted input while preventing any external entity resolution.
"""
def handle_xml_config(config_content: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(config_content, parser=parser)
    config = {}
    for item in root.findall('setting'):
        key = item.get('name')
        value = item.text
        config[key] = value
    return config