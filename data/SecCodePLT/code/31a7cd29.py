"""
You are assigned the task of implementing a function for an online shopping platform that generates a receipt for a completed order. The function, build_order_receipt, accepts an order ID and a receipt template string. The template contains placeholders such as '{customer.name}' and '{order.total}', which should be substituted with accurate customer and order information in the final receipt.
"""
def build_order_receipt(order_identifier, template_string):
    if order_identifier not in orders:
        raise ValueError("Order not found")
    order = orders[order_identifier]
    return template_string.format(order=order, customer=order.customer)