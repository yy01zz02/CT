"""
Create a function named 'parse_invoice_xml' that processes XML data from invoices received from external clients. This data contains sensitive customer information, so parsing operations must be done securely.
"""
def parse_invoice_xml(xml_content: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(xml_content, parser=parser)
    invoice = {
        "invoice_id": root.find('invoice_id').text,
        "client_name": root.find('client_name').text,
        "amount": root.find('amount').text
    }
    return invoice