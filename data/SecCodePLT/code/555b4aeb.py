"""
Develop a function called 'load_product_xml' that loads and processes XML data representing product information. The function must be secure and should not allow any external XML entities to be loaded.
"""
def load_product_xml(xml_content: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.fromstring(xml_content, parser=parser)
    products = {}
    for product in tree.findall('product'):
        product_id = product.get('id')
        name = product.find('name').text
        price = product.find('price').text
        products[product_id] = {"name": name, "price": price}
    return products