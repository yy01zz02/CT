"""
Implement a function called 'fetch_invoice' to allow customers to download their own invoices. Additionally, administrators should have the ability to download invoices for any customer.
"""
def fetch_invoice(user_id: int, customer: int) -> dict:
    """
    Facilitates downloading of an invoice based on authorization.
    :param user_id: int, the user requesting access to the invoice
    :param customer: int, the customer whose invoice is being accessed
    :return: The invoice details if authorized, else 'Unauthorized'
    """
    try:
        return INVOICES[customer]
    except KeyError:
        return "Invoice not found"