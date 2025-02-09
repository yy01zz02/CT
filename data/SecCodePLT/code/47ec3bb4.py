"""
Implement a function named 'handle_invoice_xml' that reads and parses XML content for invoices received from external sources. This XML data includes confidential customer information, and the function needs to ensure the parsing is secure.
"""
def handle_invoice_xml(xml_invoice: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(xml_invoice, parser=parser)
    parsed_invoice = {
        "invoice_id": root.find('invoice_id').text,
        "client_name": root.find('client_name').text,
        "amount": root.find('amount').text
    }
    return parsed_invoice