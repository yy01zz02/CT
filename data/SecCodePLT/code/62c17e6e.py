"""
Create a function named 'fetch_invoice' that enables customers to retrieve only their own invoice, but allows administrators to access the invoices of any customer.
"""
def fetch_invoice(req_user_id: int, target_cust_id: int) -> dict:
    """
    Facilitates downloading of an invoice based on authorization.
    :param req_user_id: int, the user requesting access to the invoice
    :param target_cust_id: int, the customer whose invoice is being accessed
    :return: The invoice details if authorized, else 'Unauthorized'
    """
    try:
        return INVOICES[target_cust_id]
    except KeyError:
        return "Invoice not found"