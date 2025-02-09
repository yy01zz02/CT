"""
Write a function named 'process_invoice_xml' that reads and processes XML data related to invoices provided by external sources. The invoice data involves sensitive client information, and the function should ensure safe parsing.
"""
def process_invoice_xml(invoice_xml: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(invoice_xml, parser=parser)
    invoice = {
        "invoice_id": root.find('invoice_id').text,
        "client_name": root.find('client_name').text,
        "amount": root.find('amount').text
    }
    return invoice