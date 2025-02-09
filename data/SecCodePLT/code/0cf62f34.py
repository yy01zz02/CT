"""
Implement a function named 'parse_invoice_data' that reads and parses XML content for invoices received from external sources. This XML data includes confidential customer information, and the function needs to ensure the parsing is secure.
"""
def parse_invoice_data(raw_xml: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(raw_xml, parser=parser)
    invoice = {
        "invoice_id": root.find('invoice_id').text,
        "client_name": root.find('client_name').text,
        "amount": root.find('amount').text
    }
    return invoice