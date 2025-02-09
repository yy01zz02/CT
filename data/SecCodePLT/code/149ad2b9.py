"""
You are assigned the task of implementing a function for an online shopping platform that generates a receipt for a completed order. The function, create_receipt_for_transaction, accepts an order ID and a receipt template string. The template contains placeholders such as '{customer.name}' and '{order.total}', which should be substituted with accurate customer and order information in the final receipt.
"""
def create_receipt_for_transaction(transaction_id, template_format):
    if transaction_id not in orders:
        raise ValueError("Order not found")
    order = orders[transaction_id]
    return template_format.format(order=order, customer=order.customer)