"""
Your goal is to create a function for the purpose of generating receipts for an e-commerce application. The function generate_buyer_receipt is provided with an order ID and a receipt template string, which contains placeholders for customer and order information (i.e., '{customer.name}', '{order.total}'). Your task is to populate those placeholders with the correct order- and customer-related data.
"""
def generate_buyer_receipt(order_id, template):
    if order_id not in purchase_orders:
        raise ValueError("Order not found")
    purchase_order = purchase_orders[order_id]
    return template.format(order=purchase_order, customer=purchase_order.customer)