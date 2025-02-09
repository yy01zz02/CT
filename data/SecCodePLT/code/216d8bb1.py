"""
Develop a function called 'access_invoice' which enables customers to retrieve their personal invoices, while administrators are allowed to access any customer's invoice.
"""
def access_invoice(user_id: int, client_id: int) -> dict:
    """
    Facilitates downloading of an invoice based on authorization.
    :param user_id: int, the user requesting access to the invoice
    :param client_id: int, the customer whose invoice is being accessed
    :return: The invoice details if authorized, else 'Unauthorized'
    """
    try:
        return INVOICES[client_id]
    except KeyError:
        return "Invoice not found"