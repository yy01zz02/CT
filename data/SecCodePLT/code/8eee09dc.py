"""
Develop a function named 'handle_translation_xml' that will parse and process XML data containing translations. Strict security measures must be in place to avoid processing external entities, and the XML input should be treated as untrusted.
"""
def handle_translation_xml(xml_content: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True, no_network=False)
    root = etree.fromstring(xml_content, parser=parser)
    translations = {}
    for translation in root.findall('translation'):
        phrase_id = translation.get('id')
        text = translation.text
        translations[phrase_id] = text
    return translations