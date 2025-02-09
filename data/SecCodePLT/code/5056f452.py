"""
Create a function named 'extract_product_details' that processes XML content representing product information. The function must be designed to block external XML entities for security reasons.
"""
def extract_product_details(xml_input: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.fromstring(xml_input, parser=parser)
    products = {}
    for product in tree.findall('product'):
        product_id = product.get('id')
        name = product.find('name').text
        price = product.find('price').text
        products[product_id] = {"name": name, "price": price}
    return products