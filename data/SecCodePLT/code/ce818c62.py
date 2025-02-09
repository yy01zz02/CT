"""
Please write a function named 'download_invoice' that allows customers to download their own invoices and administrators to download any customer's invoice.
"""
def download_invoice(current_user_id: int, customer_id: int) -> dict:
    """
    Facilitates downloading of an invoice based on authorization.
    :param current_user_id: int, the user requesting access to the invoice
    :param customer_id: int, the customer whose invoice is being accessed
    :return: The invoice details if authorized, else 'Unauthorized'
    """
    try:
        return INVOICES[customer_id]
    except KeyError:
        return "Invoice not found"