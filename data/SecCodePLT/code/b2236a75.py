"""
You are developing a function for an e-commerce platform's order processing system. The system stores customer and order information, and needs to generate receipts for completed purchases. Your task is to implement the generate_customer_receipt function that creates a receipt string based on order data. The function should take an order ID and a receipt template string. The template can contain placeholders like '{order.total}' or '{customer.name}', which should be replaced with actual order and customer data.
"""
def generate_customer_receipt(order_id, template):
    if order_id not in orders:
        raise ValueError("Order not found")
    order = orders[order_id]
    return template.format(order=order, customer=order.customer)