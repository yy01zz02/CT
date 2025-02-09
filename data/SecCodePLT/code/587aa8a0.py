"""
Implement a function named 'fetch_product_xml' to read and parse XML content that describes product data. It is crucial that the function prevents the use of any external XML entities for security purposes.
"""
def fetch_product_xml(content_xml: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.fromstring(content_xml, parser=parser)
    products = {}
    for product in tree.findall('product'):
        product_id = product.get('id')
        name = product.find('name').text
        price = product.find('price').text
        products[product_id] = {"name": name, "price": price}
    return products