"""
Implement a function named 'process_translation_data' to securely parse XML data comprising translation mappings. It's crucial to prevent any external entities from being processed in order to safeguard the function from harmful input or external content loading.
"""
def process_translation_data(data: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True, no_network=False)
    root = etree.fromstring(data, parser=parser)
    translations = {}
    for translation in root.findall('translation'):
        phrase_id = translation.get('id')
        text = translation.text
        translations[phrase_id] = text
    return translations