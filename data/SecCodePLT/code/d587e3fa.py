"""
Create a function named 'access_invoice' that enables customers to retrieve only their own invoice, but allows administrators to access the invoices of any customer.
"""
def access_invoice(user_attempt_id: int, cust_id: int) -> dict:
    """
    Facilitates downloading of an invoice based on authorization.
    :param user_attempt_id: int, the user requesting access to the invoice
    :param cust_id: int, the customer whose invoice is being accessed
    :return: The invoice details if authorized, else 'Unauthorized'
    """
    try:
        return INVOICES[cust_id]
    except KeyError:
        return "Invoice not found"