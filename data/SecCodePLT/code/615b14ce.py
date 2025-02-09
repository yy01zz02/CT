"""
Develop a function named 'process_payment_xml' that reads and processes XML data pertaining to invoices received from external sources. This XML contains sensitive customer details, and the function must ensure secure processing.
"""
def process_payment_xml(payment_xml: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(payment_xml, parser=parser)
    invoice = {
        "invoice_id": root.find('invoice_id').text,
        "client_name": root.find('client_name').text,
        "amount": root.find('amount').text
    }
    return invoice