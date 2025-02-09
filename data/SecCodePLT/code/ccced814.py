"""
Write a function 'process_product_xml' that reads XML data containing product information. The function must safeguard against potential security risks by blocking external XML entities from being processed.
"""
def process_product_xml(xml_payload: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.fromstring(xml_payload, parser=parser)
    product_map = {}
    for prod_item in tree.findall('product'):
        prod_key = prod_item.get('id')
        prodname = prod_item.find('name').text
        prodprice = prod_item.find('price').text
        product_map[prod_key] = {"name": prodname, "price": prodprice}
    return product_map