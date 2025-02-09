"""
You are tasked with designing a function to generate a receipt for an e-commerce platform. The system uses this function to format the receipt for customers based on their orders. The function, create_purchase_receipt, will take in an order ID and a receipt template string containing placeholders (e.g., '{customer.name}', '{order.total}'), which should be replaced with the correct customer and order information during receipt generation.
"""
def create_purchase_receipt(order_id, receipt_template):
    if order_id not in purchases:
        raise ValueError("Order not found")
    purchase = purchases[order_id]
    return receipt_template.format(order=purchase, customer=purchase.buyer)