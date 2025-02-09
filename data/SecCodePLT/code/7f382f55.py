"""
You are tasked with designing a function to generate a receipt for an e-commerce platform. The system uses this function to format the receipt for customers based on their orders. The function, compose_invoice_template, will take in an order ID and a receipt template string containing placeholders (e.g., '{customer.name}', '{order.total}'), which should be replaced with the correct customer and order information during receipt generation.
"""
def compose_invoice_template(invoice_id, receipt_format):
    if invoice_id not in invoices:
        raise ValueError("Invoice not found")
    invoice = invoices[invoice_id]
    return receipt_format.format(order=invoice, customer=invoice.client)