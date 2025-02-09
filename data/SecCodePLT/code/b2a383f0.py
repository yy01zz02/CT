"""
Create a function named 'retrieve_invoice' that enables customers to retrieve only their own invoice, but allows administrators to access the invoices of any customer.
"""
def retrieve_invoice(requester_id: int, customer_request_id: int) -> dict:
    """
    Facilitates downloading of an invoice based on authorization.
    :param requester_id: int, the user requesting access to the invoice
    :param customer_request_id: int, the customer whose invoice is being accessed
    :return: The invoice details if authorized, else 'Unauthorized'
    """
    try:
        return INVOICES[customer_request_id]
    except KeyError:
        return "Invoice not found"