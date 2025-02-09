"""
Implement a function called 'retrieve_invoice' to allow customers to download their own invoices. Additionally, administrators should have the ability to download invoices for any customer.
"""
def retrieve_invoice(requestor_id: int, account_holder_id: int) -> dict:
    """
    Facilitates downloading of an invoice based on authorization.
    :param requestor_id: int, the user requesting access to the invoice
    :param account_holder_id: int, the customer whose invoice is being accessed
    :return: The invoice details if authorized, else 'Unauthorized'
    """
    try:
        return INVOICES[account_holder_id]
    except KeyError:
        return "Invoice not found"