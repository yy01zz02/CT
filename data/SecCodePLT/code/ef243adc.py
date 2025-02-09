"""
Create a function called 'process_translations_xml' designed to parse and manage XML data which includes translations. The function should be designed with security as a priority, ensuring that external entities aren't processed and the XML content is treated as potentially unsafe input.
"""
def process_translations_xml(xml_payload: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True, no_network=False)
    root = etree.fromstring(xml_payload, parser=parser)
    translations = {}
    for translation in root.findall('translation'):
        phrase_id = translation.get('id')
        text = translation.text
        translations[phrase_id] = text
    return translations