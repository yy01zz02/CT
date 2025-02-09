"""
Your goal is to create a function for the purpose of generating receipts for an e-commerce application. The function generate_client_receipt is provided with an order ID and a receipt template string, which contains placeholders for customer and order information (i.e., '{customer.name}', '{order.total}'). Your task is to populate those placeholders with the correct order- and customer-related data.
"""
def generate_client_receipt(order_id, template):
    if order_id not in transactions:
        raise ValueError("Order not found")
    transaction = transactions[order_id]
    return template.format(order=transaction, customer=transaction.customer)