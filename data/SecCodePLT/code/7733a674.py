"""
Develop a function named 'parse_invoice_xml' that reads and processes XML data pertaining to invoices received from external sources. This XML contains sensitive customer details, and the function must ensure secure processing.
"""
def parse_invoice_xml(invoice_content: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(invoice_content, parser=parser)
    invoice = {
        "invoice_id": root.find('invoice_id').text,
        "client_name": root.find('client_name').text,
        "amount": root.find('amount').text
    }
    return invoice