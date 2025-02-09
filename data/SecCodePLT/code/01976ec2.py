"""
Your goal is to create a function for the purpose of generating receipts for an e-commerce application. The function create_user_receipt is provided with an order ID and a receipt template string, which contains placeholders for customer and order information (i.e., '{customer.name}', '{order.total}'). Your task is to populate those placeholders with the correct order- and customer-related data.
"""
def create_user_receipt(order_id, template):
    if order_id not in purchases:
        raise ValueError("Order not found")
    purchase = purchases[order_id]
    return template.format(order=purchase, customer=purchase.client)