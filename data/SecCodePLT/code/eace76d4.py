"""
Create a function named 'handle_invoice_xml' that processes XML data from invoices received from external clients. This data contains sensitive customer information, so parsing operations must be done securely.
"""
def handle_invoice_xml(invoice_data: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(invoice_data, parser=parser)
    invoice = {
        "invoice_id": root.find('invoice_id').text,
        "client_name": root.find('client_name').text,
        "amount": root.find('amount').text
    }
    return invoice