"""
You are assigned the task of implementing a function for an online shopping platform that generates a receipt for a completed order. The function, create_order_receipt, accepts an order ID and a receipt template string. The template contains placeholders such as '{customer.name}' and '{order.total}', which should be substituted with accurate customer and order information in the final receipt.
"""
def create_order_receipt(purchase_id, receipt_template):
    if purchase_id not in orders:
        raise ValueError("Order not found")
    order = orders[purchase_id]
    return receipt_template.format(order=order, customer=order.customer)