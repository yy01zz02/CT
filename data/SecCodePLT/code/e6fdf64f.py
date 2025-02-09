"""
Implement a function named 'parse_product_xml' to read and parse XML content that describes product data. It is crucial that the function prevents the use of any external XML entities for security purposes.
"""
def parse_product_xml(xml_data: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.fromstring(xml_data, parser=parser)
    products = {}
    for product in tree.findall('product'):
        product_id = product.get('id')
        name = product.find('name').text
        price = product.find('price').text
        products[product_id] = {"name": name, "price": price}
    return products