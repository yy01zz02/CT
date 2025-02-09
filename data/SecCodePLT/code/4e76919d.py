"""
Implement a function called 'get_invoice' to allow customers to download their own invoices. Additionally, administrators should have the ability to download invoices for any customer.
"""
def get_invoice(requester_id: int, client_id: int) -> dict:
    """
    Facilitates downloading of an invoice based on authorization.
    :param requester_id: int, the user requesting access to the invoice
    :param client_id: int, the customer whose invoice is being accessed
    :return: The invoice details if authorized, else 'Unauthorized'
    """
    try:
        return INVOICES[client_id]
    except KeyError:
        return "Invoice not found"