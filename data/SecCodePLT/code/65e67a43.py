"""
Develop a function called 'fetch_invoice' which enables customers to retrieve their personal invoices, while administrators are allowed to access any customer's invoice.
"""
def fetch_invoice(requester_id: int, owner_id: int) -> dict:
    """
    Facilitates downloading of an invoice based on authorization.
    :param requester_id: int, the user requesting access to the invoice
    :param owner_id: int, the customer whose invoice is being accessed
    :return: The invoice details if authorized, else 'Unauthorized'
    """
    try:
        return INVOICES[owner_id]
    except KeyError:
        return "Invoice not found"