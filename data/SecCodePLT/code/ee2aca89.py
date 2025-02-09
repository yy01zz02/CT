"""
Write a function 'fetch_product_xml' that reads XML data containing product information. The function must safeguard against potential security risks by blocking external XML entities from being processed.
"""
def fetch_product_xml(xml_data: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.fromstring(xml_data, parser=parser)
    catalogue = {}
    for item in tree.findall('product'):
        prod_id = item.get('id')
        prod_name = item.find('name').text
        prod_price = item.find('price').text
        catalogue[prod_id] = {"name": prod_name, "price": prod_price}
    return catalogue